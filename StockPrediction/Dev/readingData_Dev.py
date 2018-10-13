import pandas as pd
import os


DataFile        = os.path.join (os.getcwd(),'../DataFiles/train.txt')
Data_Handle     = open (DataFile)
Data_text       = Data_Handle.read()


StocksData_text       = Data_text.split('\n')[:-1]
StockNames       = [Stock.split() [0] for Stock in StocksData_text]
StockData        = [Stock.split() [1:] for Stock in StocksData_text]

StockData_DF    =  pd.DataFrame (index = StockNames, data = StockData)
DataOut         =  os.path.join (os.getcwd(),'../DataFiles/StockData.csv')
StockData_DF.to_csv (DataOut,index = True,header=False)
