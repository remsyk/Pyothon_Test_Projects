
import os
#In this file created in step 1, write python code using sqlite3 to:
import sqlite3
from contextlib import closing
from collections import defaultdict
from Blair_Scott_Project_Part1 import BaseballCSVReader

#Create a “create_dbs.py” file.
def create_db():
    #Create a “baseball.db” database
    with closing(sqlite3.connect('baseball.db')) as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Baseball_stats")
        #Create 1 table named “baseball_stats” with the following columns:
        '''
        The "baseball.db" SQLite3 database should look like this:
         Baseball_stats
            ========================
            player_name         text
            games_played        int
            average             real
            salary              real
        '''
        cursor.execute("CREATE TABLE Baseball_stats("
                  "player_name      TEXT,"
                  "salary           INT,"
                  "games_played     REAL,"
                  "average           REAL)")

def insert(records, cursor):

    #Insert each record in a list of ``records`` into the database.
    # For each record in the list, write and execute an INSERT INTO statement to save the record's information to the correct table.
    # For each row fetched, iterate with a for loop over the result of your select command
    for i in records:
        # Example for baseball: cursor.execute(“INSERT INTO baseball_stats VALUES( ?, ?, ?, ?)”, (name, number_games_played, avg, salary))
        cursor.executemany("INSERT INTO Baseball_stats VALUES(?,?,?,?)", (i,))

def select(cursor):
    selectList =[]
    # write and execute a SELECT statement to get all the records of the table for the DAO
    # Example for baseball: cursor.execute(“SELECT player_name, games_played, average, salary FROM baseball_stats;”)
    # cursor.execute(“SELECT player_name, games_played, average, salary FROM baseball_stats”)
    #Select all the records from the database.
    for row in cursor.execute('SELECT * FROM Baseball_stats'):
        '''
        print("player_name ", row[0])
        print("salary ", row[1])
        print("games_played ", row[2])
        print("average ", row[3], "\n")
        '''
        selectList.append(row)
    #Return them as a list of tuples.
    return selectList


if __name__ == '__main__':
    salaries = defaultdict(list)
    create_db()

    connection = sqlite3.connect('baseball.db')
    insert(BaseballCSVReader("MLB2008.csv").__getitem__(), connection.cursor())
    select(connection.cursor())
    connection.commit()
    connection.close()
