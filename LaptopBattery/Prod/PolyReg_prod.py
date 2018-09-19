#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
np.set_printoptions(precision=2)
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")



Laptop   = pd.read_table ('trainingdata.txt',sep =',',header = None, names =      ['Predictor','Responce'])
Laptop ['Predictor'] = Laptop ['Predictor'].apply (lambda x : float (x))
Laptop ['Responce']  = Laptop ['Responce'].apply (lambda x : float (x))
X_F1 = (np.array (Laptop ['Predictor']).reshape (-1,1))
y_F1 = (np.array (Laptop ['Responce']).reshape (-1,1))
poly = PolynomialFeatures(degree=11)
X_F1_poly = poly.fit_transform(X_F1)
X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,random_state = 0)
linreg   = LinearRegression().fit(X_train, y_train)
NewData     = 0.09
NewData_Poly= poly.fit_transform(NewData)
Predictions = linreg.predict(NewData_Poly)


if __name__ == '__main__':
    timeCharged = float(input())
    #print (Laptop)
    NewData_Poly= poly.fit_transform(timeCharged)
    Predictions = linreg.predict(NewData_Poly)
    print(*np.round(Predictions.ravel(),2),sep='\n')
