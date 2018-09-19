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

#
path = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/ReadingData/Data'


##Reading Input Data
inputData = pd.read_csv ('input03.txt',delim_whitespace =True, header =None , names = ['Predictor1','Predictor2','Responce'])


##Training Data
F = int (inputData.iloc[0] [0])
N = int (inputData.iloc[0] [1])
TrainingData = inputData [1:N+1]
TrainingData.reset_index(inplace=True)
Predictors  = ['Predictor' + str(i) for i in range (1,F+1)]
Responce    = ['Responce']
TrainingData_Predictors = TrainingData  [Predictors]
TrainingData_Responce  = TrainingData [Responce]
TrainingData_Responce.to_csv (path+'TrainingData_Responce.csv',index=False)
TrainingData_Predictors.to_csv (path+'TrainingData_Predictors.csv',index=False)


##Test Data
T = inputData.iloc [N+1] [0]
TestData = inputData [N+2:]
TestData.reset_index(inplace=True)
TestData_Predictors = TestData [Predictors]
TestData_Responce  = pd.read_csv ('output03.txt', header =None , names = ['Responce'])
TestData_Responce.to_csv (path+'TestData_Responce.csv',index=False)
TestData_Predictors.to_csv (path+'TestData_Predictors.csv',index=False)
