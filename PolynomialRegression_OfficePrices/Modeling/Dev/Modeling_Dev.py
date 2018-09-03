import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
np.set_printoptions(precision=2)

DataPath = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/Modeling/Data/'
X_F1  =  pd.read_csv (DataPath+'TrainingData_Predictors.csv')
Y_F1  =  pd.read_csv (DataPath+ 'TrainingData_Responce.csv')
y_F1  = Y_train ['Responce']

poly = PolynomialFeatures(degree=2)
X_F1_poly = poly.fit_transform(X_F1)
X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,random_state = 0)
linreg   = LinearRegression().fit(X_train, y_train)
