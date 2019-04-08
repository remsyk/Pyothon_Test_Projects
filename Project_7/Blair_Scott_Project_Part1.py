import os.path
import csv
from Tools.scripts.treesync import raw_input


#Create class: AbstractRecord, This class will contain 1 (instance) member: name
class AbstractRecord:
    def __init__(self,name):
        self.name = name


#Create a record class for each of the files you want to load., i.e. BaseballStatRecord and StockStatRecord.
class StockStatRecord(AbstractRecord):
    # And including the following functionality: inherit the AbstractRecord, have an initializer method that takes the data you want to load as arguments
    # For stocks:Stock symbol (ticker)→ this should be stored in the “name” member,Company name (company_name),Exchange country (exchange_country),Stock Price (price),Exchange Rate (exchange_rate),Shares Outstanding (shares_outstanding),Net Income (net_income),Market Value in USD (market_value_usd) – This value is calculated in step 4e, Price/Earnings Ratio (pe_ratio) – This step is calculated in step 4e
    def __init__(self, name,exchange_country,company_name,price,exchange_rate,shares_outstanding,net_income,market_value_usd, pe_ratio):
        self.l=[name,exchange_country,company_name,price,exchange_rate,shares_outstanding,net_income,
                 market_value_usd, pe_ratio]
        self.writeTo("StockStatRecord.csv",self.l,'a')
        #self.__str__()

    # For each record type, override __str__() (https://docs.python.org/3/reference/datamodel.html#object.__str__ ) to return a string of the form: “<name of the record type> ( <value1>, <value2>,  <...> )” using “str.format”.
    def __str__(self):
        # For floats please only display 2 decimal numbers (2 numbers after the comma)

        myStr = "StockStatRecord({0}{1}{2}{3}{4}{5}{6}{7}{8})".format(self.l[0],self.l[1],self.l[2],"{:.2f}".format(float(self.l[3])),"{:.2f}".format(float(self.l[4])),"{:.2f}".format(float(self.l[5])),"{:.2f}".format(float(self.l[6])),"{:.2f}".format(float(self.l[7])),"{:.2f}".format(float(self.l[8])))
        print(myStr)

    def writeTo(self, fileName, words, type):
        with open(fileName, type, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(words)
        f.close()


#Create a record class for each of the files you want to load., i.e. BaseballStatRecord and StockStatRecord.
class BaseballStatRecord(AbstractRecord):
    # And including the following functionality: inherit the AbstractRecord, have an initializer method that takes the data you want to load as arguments
    # for baseball,player name → this should be stored in the “name” member,salary,G (Games played),AVG (which is the batting average)
    def __init__(self, name, salary, G, AVG):
        super().__init__(name)
        self.l = [name,salary,G,AVG]
        self.writeTo("BaseballStatRecord.csv",self.l,'a')
        #self.__str__()

    # For each record type, override __str__() (https://docs.python.org/3/reference/datamodel.html#object.__str__ ) to return a string of the form: “<name of the record type> ( <value1>, <value2>,  <...> )” using “str.format”.
    def __str__(self):
        myStr = "BaseballStatRecord({0},{1},{2},{3},)".format(self.l[0], self.l[1], self.l[2], "{:.2f}".format(float(self.l[3])))
        print(myStr)

    def writeTo(self,fileName, words, type):
        with open(fileName, type, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(words)
        f.close()


#Create 1 AbstractCSVReader class
class AbstractCSVReader:
    # The class should have an initializer method taking the path to the file to be read
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    # The class should have the method: row_to_record(row). Where “row” is a row from the CSV as a dictionary
    def row_to_record(self, row):
        # This method should be implemented by simply raising NotImplementedError.
        try:
            #if row has now data
            if row is None:
                raise NotImplementedError("TypeError: row is not loading")
        except NotImplemented:
            return row


    # The class should have the method: load() that returns a list of records. Load should:
    def load(self):
        # Return a list of items from file
        # Use “with” to open the CSV files
        with open(self.path_to_file, 'r') as f:
            reader = csv.reader(f)
            #iterates through every row and returns
            next(f)
            # read each row from the file into a list
            for row in reader:
                # call the row_to_record method and send the row as a parameter
                self.row_to_record(row)
        f.close()


#Create a CSV reader class for each of the files you want to load,i.e. BaseballCSVReader and StocksCSVReader. The class should inherit the AbstractCSVReader
class BaseballCSVReader(AbstractCSVReader):
    fullRecord=[]
    # Each class should implement its own row_to_record method.
    def row_to_record(self, row):
        super().row_to_record(row)
        # The input is a list of unvalidated data, it should validate the data, parse it, create new record and return the record created. (Hint: a tuple if a good structure to use for records)
        try:
            # Validation fails for any row that is missing any piece of information
            if '' in row[1:]:
                raise BadData("TypeError: row is missing item")
            # Validation fails if the name (symbol or player name) is empty
            if not row[0]:
                 # handle the BadData exception raised by  row_to_record by skipping the record – For more on BadData Exception see step 5
                raise BadData("TypeError: first row is missing item")
            # Validation fails if any of the numbers (int or float) cannot be parsed (watch out of the division by zero!!)
            if isinstance(row[2:], str):
                raise BadData("TypeError: the numbers (int or float) cannot be parsed")
        # If validation fails: this method should raise a BadData exception (requirement #5)
        except BadData:
            pass
        else:
            # If no exception is raised: then the record should be added to the list of records.
            self.record = (row[0], row[2], row[5], row[68])
            #BaseballStatRecord(row[0], row[2], row[5], row[68])
            # Print each record to the console. You are to use: print(record)
            #print(self.record)
            # Once all records are loaded into the list, returns the list.
            self.fullRecord.append(self.record)
            return self.fullRecord
    def __getitem__(self):
        self.load()
        return self.fullRecord


#Create a CSV reader class for each of the files you want to load,i.e. BaseballCSVReader and StocksCSVReader. The class should inherit the AbstractCSVReader
class StocksCSVReader(AbstractCSVReader):
    fullRecord=[]
    # Each class should implement its own row_to_record method.
    def row_to_record(self, row):
        super().row_to_record(row)
        try:
            # Validation fails for any row that is missing any piece of information
            if '' in row[1:]:
                raise BadData("TypeError: row is missing item")
            # Validation fails if the name (symbol or player name) is empty
            if not row[0]:
                # handle the BadData exception raised by  row_to_record by skipping the record – For more on BadData Exception see step 5
                raise BadData("TypeError: first row is missing item")
            #Validation fails if any of the numbers (int or float) cannot be parsed (watch out of the division by zero!!)
            if isinstance(row[2:], str):
                raise BadData("TypeError: the numbers (int or float) cannot be parsed")

        # If validation fails: this method should raise a BadData exception (requirement #5)
        except BadData:
            pass
        else:
            # [name, exchange_country, company_name, price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio]

            if isinstance(row[3], str):
                row[3] = float(row[3])
            if isinstance(row[4], str):
                row[4] = float(row[4])
            if isinstance(row[5], str):
                row[5] = float(row[5])
            if isinstance(row[6], str):
                row[6] = float(row[6])

            # StocksCSVReader should have two calculations using the extracted records:
            # market_value_usd = Price * ExchangeRate * SharesOutstanding
            market_value_usd = row[3] * row[4] * row[5]
            # pe_ratio = Price * SharesOutstanding / NetIncome
            pe_ratio = row[3] * row[5] / row[6]

            row.extend((market_value_usd, pe_ratio))

            # If no exception is raised: then the record should be added to the list of records.
            self.record = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
            #StockStatRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            # Print each record to the console. You are to use: print(record)
            #print(record)
            # Once all records are loaded into the list, returns the list.
            self.fullRecord.append(self.record)
            return self.fullRecord
    def __getitem__(self):
        self.load()
        return self.fullRecord


#Create a BadData custom exception to handle record creation errors
class BadData(Exception):
    def __init__(self, message):
        print(message)



################################################

#From your main section ( https://docs.python.org/3/library/__main__.html )load the CSV (e.g.  BaseballCSVReader('path to my CSV').load())

if __name__ == "__main__":
    # execute only if run as a script
    BaseballCSVReader("MLB2008.csv").load()
    StocksCSVReader("StockValuations.csv").load()