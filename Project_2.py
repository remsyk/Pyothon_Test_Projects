'''
This file is a template that may be used for Assignment 2.  The intent is to supply
you with some code so you can focus on the new items in the program
'''
import os
import random
import os.path
import csv
import sys

folder = "resouces"
fileDir = os.path.abspath(folder)
fileDir += "\\"

def load_csv_to_list(path_to_file):
    # Validate Path to file exist
    # Validate file exists
    path_to_file = fileDir + path_to_file
    if os.path.exists(path_to_file) == True:
        print(path_to_file, "OK!")

    # Return a list of items from file
    with open(path_to_file) as f:
        reader = csv.reader(f)
        my_list = list(reader)
        f.close()
    return my_list


def shuffle(sequence):
    # 'Returns a shuffled list'
    # Write the code that will take a list and shuffle it randomly
    l = len(sequence) - 1
    for i in range(3):
        k = random.randint(0, l)
        sequence[k], sequence[l] = sequence[l], sequence[k]
    return sequence


def load_mad_lib_resource(path_to_resource):
    # Call load_csv_to_list
    # Verify the file exists
    # Return a tuple of the shuffled list
    return tuple(shuffle(load_csv_to_list(path_to_resource)[0])) #all you need is this line


def writeTo(fileName, words, type):
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(fileDir + "\\" + fileName, type, newline='') as f:
        writer = csv.writer(f)
        writer.writerow(words)
    f.close()


def play_game(username):
    # create an list that contains all the sentences that will be used for the mad libs, with element in place of where I want to insert words
    while True:
        while True:
            noun = load_mad_lib_resource("noun.csv")
            verb = load_mad_lib_resource("verb.csv")
            adjective = load_mad_lib_resource("adjective.csv")
            sentences = list(load_mad_lib_resource("sentences.csv"))

            arrOrder = [noun, verb, adjective]
            blank = 0
            blank = int(input("Please Select a Number: "))
            test = []
            mad = []
            mad2 = []
            mad1 = []
            happy = None
            blank2 = blank
            blank3 = blank
            blank4 = blank
            indices = None

            for i in range(5):
                sentences[i] = list(sentences[i].split(" "))

            if blank < 0:
                continue
            if blank > 100:
                blank /= 10

            if blank > 4:
                blank2 = blank % len(sentences)
                blank3 = blank % len(arrOrder[1])
                blank4 = blank % len(arrOrder[2])
                blank %= len(arrOrder[0])
                indices = [j for j, x in enumerate(sentences[blank2]) if x == '_']

            elif blank < 5:
                indices = [j for j, x in enumerate(sentences[blank2]) if x == '_']

            inputList = [blank, blank3, blank4]
            mad1 = sentences[blank2]
            for j in range(3):
                mad1[indices[j]] = arrOrder[j][inputList[j]]

            mad = sentences[blank2]
            mad2 = ' '.join(sentences[blank2])
            print(mad2)
            mad3 = [mad2, len(load_csv_to_list(username))]

            if mad in load_csv_to_list(username):
                print("Madlib Is Not Unique!")

            else:
                print("Madlib Is Unique!")
                writeTo(username, mad3, 'a')


            # find out if input is unique and if so save to a list
            # ask is user is happy
            happy = input("Are you Happy with your mad lib? [y/n]: ")
            # if user is happy, exit
            if 'n' in happy:
                continue
            # else restart
            else:
                break
        break
    return mad2


# GET THE LISTS FROM THE FILES
#This code works, it only needs to run one time because the files already exist. Simply take out comments to verify code words

sentences1 = ["_ was _ in an _ battle.",
                  "There was no _ to _ _",
                  "_ tried to _ for the right to live _",
                  "When the _ _ to decide _ the color of the drapes",
                  "The story of _ would _ throughout the city and be told by _ people"]
verb1 = ['escape', 'fly', 'cheese-it', 'fall', 'die', 'suffocate', 'abduct', 'win', 'love']
noun1 = ['butterfly', 'banana', 'weak', 'underpants', 'box', 'moon']
adjective1 = ['smooth', 'old', 'yellow', 'buttery', 'bright']

writeTo("noun.csv", noun1, 'w')
writeTo("verb.csv", verb1, 'w')
writeTo("adjective.csv", adjective1, 'w')
writeTo("sentences.csv", sentences1, 'w')


# VERIFY THE LISTS EXIST
#This code works, it can be found in the play_game function. Simply take out comments to verify code words, each function returns ok of file exists


# PROMPT FOR USERNAME
username = input("Please Enter Username: ")
# VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM
if username == '':
    sys.exit(0)
ext = ".csv"
username += ext

# FIND OUT IF THERE IS AN EXISTING USER SAVED GAMES
if os.path.exists(fileDir + username) == True:
    # user's mad lib
    # GET THE USER'S SAVED GAMES IF IT EXISTS
    user_sentences = (load_csv_to_list(username))
    print(user_sentences)
    # CALL PLAY GAME FUNCTION
    play_game(username)

else:
    print("New User Account Created")
    # CALL PLAY GAME FUNCTION
    with open(fileDir + username, 'w'):
        pass
    play_game(username)



# SORT THE USER SENTENCES
#shuffle of worlds is handled in play_game function

print("Bye!")
