import sys
import os
#creat an list that contains all the sentences that will be used for the mad libs, with element in place of where I want to insert words
mad = '_ was locked in an epic battle of the _ \n There was no hope to _ \n but this _ _ battled on for the right to be called _ \n When the council of _ sat down to decide the fate of the _ ' \
         'it was to late \n because they had already failed to _ \n The story of the _ would be told throughout the _ \n cherishing the struggle of _ \n -The End-'
#print array so user can read it
print(mad)
#convert the list so every character holds its own index so i can parse and edit it easier later
mad = list(mad.split(" "))

#find all blank elements in the madlibs list
indices = [i for i, x in enumerate(mad) if x == "_"]
#declare 4 lists containing nouns, verbs, adjectives, and pronouns
verbs = ['escape', 'fly', 'cheese-it', 'fall', 'die', 'suffocate', 'abduct', 'win', 'love']
nouns = ['butterfly', 'banana', 'week', 'underpants', 'box', 'moon']
adjective = ['smooth', 'old', 'yellow', 'buttery']
properNouns = ['Chef', 'Susan', 'Pope', 'Canada', "Monday"]
#creat 2 lists for the ordering of user input messages and order of array elements they will be selecting from through request
kindOrder = ['Proper Noun[1-4]: ', 'Noun[1-5]: ', 'Verb[1-8]: ', 'Adjective[1-3]', 'Proper Noun[1-4]: ', 'Proper Noun[1-4]: ', 'Proper Noun[1-4]: ', 'Noun[1-5]: ', 'Verb[1-8]: ', 'Noun[1-5]: ', 'Noun[1-5]: ', 'Proper Noun[1-4]: ']
arrOrder = [properNouns, nouns, verbs, adjective, properNouns, properNouns, properNouns, nouns, verbs, nouns, nouns, properNouns]
test = []
while True:
    while True:
        i = 0
        #while loop to run for the number of elements in the madlibs list
        while i < 12:
            #ask for user input and convert to int, with message that changes based on needed word type (ex. adj, verb)
            blank = int(input(kindOrder[i]))
            #set element to changing word type list list
            wordType = arrOrder[i]
            #if input is less than elements in list let input go through as is
            if blank < len(wordType):
                blank1 = blank
            #else if it is greater, get the remainder of the length of the lis from input (input % length_of_list)
            else:
                blank1 = blank % len(wordType)
            #edit mad libs list with input
            mad[indices[i]] = wordType[blank1]

            i += 1
            #restart game if user makes invalid input
            if blank < 0:
                print("Invalid Input, Try Again, From The Top!")
                i -= 1
                break

        mad2 = ' '.join(mad)
        print(mad2.replace(',', '\n'))

        if mad2 in test:
            print("Madlib Is Not Unique!")
        else:
           test.append(mad2)
           print("Madlib Is Unique!")

        # find out if input is unique and if so save to a list
        # ask is user is happy
        happy = input("Are you Happy with your mad lib? [y/n]: ")
        # if user is happy, exit
        if 'y' in happy:
            sys.exit(0)
        # else restart
        else:
            break


