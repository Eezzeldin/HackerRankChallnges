'''
Author: Emad Ezzeldin
Date  : Sunday September 2nd 2018
Challenge: Polynomial Regression
Fit a PolyReg model on 2 predictors and one responce variable.
'''

##Package Imports
import os
import sys
import pandas as pd


##Setting the path
ProblemDir = os.path.join (os.getcwd(), '..' , '..','predicting-office-space-price-testcases')
DataDir    = os.path.join (ProblemDir , 'input')
sys.path.append (DataDir)
#print (sys.path)


##Reading Input Data
inputData = pd.read_csv ('input03.txt',delim_whitespace =True, header =None , names = ['Predictor1','Predictor2','Responce'])
print ("=="*40)
print ("InputData",'\n')
print (inputData)


##Training Data
#Number of Predictors
F = int (inputData.iloc[0] [0])
print ("=="*40)
print ("Number of Predictors: ", F)
#Number of Training Rows
N = int (inputData.iloc[0] [1])
print ("=="*40)
print ("Number of Training Rows: ", N)
#Getting Training Data out of the noise of input data
TrainingData = inputData [1:N+1]
TrainingData.reset_index(inplace=True)
print ("=="*40)
print ("TrainingData",'\n')
print (TrainingData)
#Specifying Predictor and Responce Columns
Predictors  = ['Predictor' + str(i) for i in range (1,F+1)]
Responce    = ['Responce']
#Predictors Varibales Columns
TrainingData_Predictors = TrainingData  [Predictors]
print ("=="*40)
print ("TrainingData_Predictors",'\n')
print (TrainingData_Predictors)
#Outputing TrainingData Predictors
print ("=="*40)
print ('Outputing TestData_Predictors')
TrainingData_Predictors.to_csv ('TrainingData_Predictors.csv',index=False)
print ('Outputed TrainingData_Predictors')
#Responce Variable Column
TrainingData_Responce  = TrainingData [Responce]
print ("=="*40)
print ("TrainingData_Responce",'\n')
print (TrainingData_Responce)
#Outputing Training Data Responce
print ("=="*40)
print ('Outputing TrainingData_Responce')
TrainingData_Responce.to_csv ('TrainingData_Responce.csv',index=False)
print ('Outputed TrainingData_Responce ')


##Test Data
#Number of Test Data Rows
T = inputData.iloc [N+1] [0]
print ("=="*40)
print ('Number of Test Data Rows: ', T)
#Extracting Test Data from input data
TestData = inputData [N+2:]
TestData.reset_index(inplace=True)
print ("=="*40)
print ("TestData",'\n')
print (TestData)
#Extracting Predictor Columns
TestData_Predictors = TestData [Predictors]
print ("=="*40)
print ("TestData_Predictors",'\n')
print (TestData_Predictors)
#Outputing TestData_Predictors
print ("=="*40)
print ('Outputing TestData_Predictors')
TestData_Predictors.to_csv ('TestData_Predictors.csv',index=False)
print ('Outputed TestData_Predictors ')

#Reading Test Data Responce Column
TestData_Responce  = pd.read_csv ('output03.txt', header =None , names = ['Responce'])
print ("=="*40)
print ("TestData_Responce",'\n')
print (TestData_Responce)
#Outputing TestData_Responce
print ("=="*40)
print ('Outputing TestData_Responce')
TestData_Responce.to_csv ('TestData_Responce.csv',index=False)
print ('Outputed TestData_Responce')
