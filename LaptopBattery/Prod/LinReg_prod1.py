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
Laptop   = Laptop [Laptop ['Responce'] < 8]



X_R1 = (np.array (Laptop ['Predictor']).reshape (-1,1))
y_R1 = (np.array (Laptop ['Responce']).reshape (-1,1))

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)
linreg = LinearRegression().fit(X_train, y_train)



if __name__ == '__main__':
    timeCharged = float(input())
    if timeCharged < 4.00:
        Predictions = linreg.predict(timeCharged)
        print(*np.round(Predictions.ravel(),2),sep='\n')
    else:
        print (8)
