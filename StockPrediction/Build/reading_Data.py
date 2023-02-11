import pandas as pd
import os


DataFile        = os.path.join (os.getcwd(),'../DataFiles/train.txt')
Data_Handle     = open (DataFile)
Data_text       = Data_Handle.read()
print ("=="*40)
print (Data_text)
print ("=="*40)

StocksData_text       = Data_text.split('\n')[:-1]
print ("=="*40)
print (StocksData_text[0])
print (StocksData_text[5])
print (StocksData_text[-1])
print ("=="*40)

StockNames       = [Stock.split() [0] for Stock in StocksData_text]
print (StockNames)
StockData        = [Stock.split() [1:] for Stock in StocksData_text]
print (StockData)

StockData_DF    =  pd.DataFrame (index = StockNames, data = StockData)
print (StockData_DF)
