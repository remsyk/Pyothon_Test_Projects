
import os
#In this file created in step 1, write python code using sqlite3 to:
import sqlite3
from contextlib import closing
from collections import Counter
from Blair_Scott_Project_Part1 import StocksCSVReader


def create_db():
    # Create a “stocks.db” database:
    with closing(sqlite3.connect('stocks.db')) as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS stcoks_stats")
        # Create 1 table named “stock_stats”
        # [name, exchange_country, company_name, price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio]
        '''
        The " stocks.db" SQLite3 database should look like this:
            stock_stats
            ========================
            company_name            text
            ticker                  text
            country                 text
            price                   real
            exchange_rate           real
            shares_outstanding      real
            net_income              real
            market_value            real
            pe_ratio                real
        '''
        cursor.execute("CREATE TABLE stocks_stats("
                  "ticker               TEXT,"
                  "exchange_country     TEXT,"
                  "comapny_name         TEXT,"
                  "price                REAL, "
                  "exchange_rate        REAL,"
                  "shares_outstanding   REAL,"
                  "net_income           REAL,"
                  "market_value         REAL, "
                  "pe_ratio             REAL)")

def insert(records, cursor):

    #Insert each record in a list of ``records`` into the database.
    for i in records:
        cursor.executemany("INSERT INTO stocks_stats VALUES(?,?,?,?,?,?,?,?,?)", (i,))

def select(cursor):
    selectList = []
    # write and execute a SELECT statement to get all the records of the table for the DAO
    #Select all the records from the database.
    for row in cursor.execute('SELECT * FROM stocks_stats'):
        '''
        print("ticket ", row[0])
        print("exchange_country ", row[1])
        print("company_name ", row[2])
        print("price ", row[3])
        print("exchange_rate ", row[4]),
        print("shares_outstanding ", row[5]),
        print("net_income ", row[6]),
        print("market_value ", row[7]),
        print("pe_ratio ", row[8], "\n")
        '''
        selectList.append(row)

    #Return them as a list of tuples.
    return selectList


if __name__ == '__main__':
    counts = Counter()
    create_db()

    connection = sqlite3.connect('stocks.db')
    insert(StocksCSVReader("StockValuations.csv").__getitem__(), connection.cursor())
    select(connection.cursor())
    connection.commit()
    connection.close()


