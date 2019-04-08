import sqlite3
import baseball
import stocks
from Blair_Scott_Project_Part1 import BaseballStatRecord, BaseballCSVReader, StocksCSVReader
from Blair_Scott_Project_Part1 import StockStatRecord
from collections import defaultdict, Counter


#Create AbstractDAO class. It should have the methods:
class AbstractDAO:
    #it should have 1 (instance) member: db_name
    def __init__(self, db_name):
        self.db_name = db_name

    #insert_records(records) – Should raise the NotImplementedError
    def insert_records(self, records):
        # call the method connect(),using the returned connection, create a cursor.
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    #select_all() - Should raise the NotImplementedError
    def select_all(self):
        # call the method connect(), using the returned connection, create a cursor.
        self.cursor = self.connect().cursor()


    def connect(self):
        # connect to the database identified by db_name
        # returns the created connection
        return sqlite3.connect(self.db_name)


# Create  BaseballStatsDAO class
# Class should inherit AbstractDAO
class BaseballStatsDAO(AbstractDAO):

    #takes a list of records as parameter ( BaseballStatsDAO takes BaseballStatRecord)
    def insert_records(self, records):
        super().insert_records(records)
        baseball.insert(records, self.cursor)
        # Commit the connection
        self.connection.commit()
        self.connection.close()
        # Commit the connection


    def select_all(self):
        super().select_all()
        # create an empty deque to hold the records in memory
        # Add the record to the deque
        baseballDeque = sqlite3.collections.deque(baseball.select(self.cursor))

        # For each row fetched, iterate with a for loop over the result of your select command

        for row in baseball.select(self.cursor):
            #Create a new record (BaseballStatRecord)
            BaseballStatRecord(row[0],row[1],row[2],row[3])

        # Close the connection
        self.connect().close()

        # Return the deque
        return baseballDeque

#Create  StockStatsDAO class
#Class should inherit AbstractDAO
class StockStatsDAO(AbstractDAO):

    #takes a list of records as parameter ( BaseballStatsDAO takes BaseballStatRecord)
    def insert_records(self, records):
        super().insert_records(records)
        stocks.insert(records, self.cursor)
        # Commit the connection
        self.connection.commit()
        # Close the connection
        self.connection.close()

    def select_all(self):
        super().select_all()
        # create an empty deque to hold the records in memory
        # Add the record to the deque

        stockDeque = sqlite3.collections.deque(stocks.select(self.cursor))

        # For each row fetched, iterate with a for loop over the result of your select command
        for row in stocks.select(self.cursor):
            #Create a new record (BaseballStatRecord)
            StockStatRecord(row[0],row[1],row[2],row[3],row[5],row[5],row[6],row[7],row[8])

        # Close the connection
        self.connect().close()

        # Return the deque
        return stockDeque


baseball.create_db()
stocks.create_db()
BaseballStatsDAO("baseball.db").insert_records(BaseballCSVReader("MLB2008.csv").__getitem__())
StockStatsDAO("stocks.db").insert_records(StocksCSVReader("StockValuations.csv").__getitem__())

#Using the instance of BaseballStatsDAO select_all the records
baseballDict={}
for row in BaseballStatsDAO("baseball.db").select_all():
    # Print the dictionary formatting the salary to 2 decimal places.
    avg = float("{:.2f}".format(float(row[3])))
    baseballDict.update({row[1]: avg})

intermediate = defaultdict(list)

#for subdict2 in d:
for key, value in baseballDict.items():
    intermediate[key].append(value)
    # Compute the average salary and enter into a dictionary by batting average
for key, value in intermediate.items():
    print(key, sum(value) / len(value))


#Using the instance of StockStatsDAO select_all the records
counter = Counter()
#Calculate and print the number of tickers by exchange_country using a dictionary.
for ticker in StockStatsDAO("stocks.db").select_all():
    counter[ticker[1]] +=1

print(counter)