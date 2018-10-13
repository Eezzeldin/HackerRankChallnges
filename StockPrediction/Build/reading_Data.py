import pandas as pd
import os


DataFile = os.path.join (os.getcwd(),'../DataFiles/train.txt')
Data     = pd.read_table(DataFile,sep='\n',header =None)
(Data.transpose().to_csv ('showme.csv'))
print ("=="*40)
print (Data)
print ("=="*40)
print (Data.iloc[2])
print ("=="*40)
print (Data.transpose())
print ("=="*40)
print (Data.values.tolist())
print ("=="*40)
DataList  = Data.values
for Data in DataList:
    Stock = Data
    StockNames = Stock [0]
    print (Stock)
    print (StockNames)
#print ([Data.values.tolist() [0][0] for stock in ])
print ("=="*40)
