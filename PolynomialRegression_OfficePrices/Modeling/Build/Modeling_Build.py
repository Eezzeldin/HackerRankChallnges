import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
np.set_printoptions(precision=2)

# synthetic dataset for more complex regression
from sklearn.datasets import make_friedman1
X_F1, y_F1 = make_friedman1(n_samples = 100,
                           n_features = 7, random_state=0)

print ("=="*40)
print ("complex reg")
print (X_F1)


DataPath = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/Modeling/Data/'
X_train  =  pd.read_csv (DataPath+'TrainingData_Predictors.csv')
Y_train  =  pd.read_csv (DataPath+ 'TrainingData_Responce.csv')
Y_train  = Y_train ['Responce']
print ('=='*40)
print ('Training Data Predictors')
print (X_train)
print ('Training Data Predictors')
print (X_train.values)
print ('=='*40)
print ('Training Data Responce')
print (Y_train)

X_F1, y_F1 = X_train.values , Y_train.values

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

X_train, X_test, y_train, y_test = train_test_split(X_F1, y_F1,
                                                   random_state = 0)

print ("X_Test")
print (X_test)
print ("y_Test")
print (y_test)

linreg = LinearRegression().fit(X_train, y_train)

print('linear model coeff (w): {}'
     .format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test, y_test)))

print('\nNow we transform the original input data to add\n\
polynomial features up to degree 2 (quadratic)\n')
poly = PolynomialFeatures(degree=2)
X_F1_poly = poly.fit_transform(X_F1)

X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,
                                                   random_state = 0)
linreg = LinearRegression().fit(X_train, y_train)

print('(poly deg 2) linear model coeff (w):\n{}'
     .format(linreg.coef_))
print('(poly deg 2) linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('(poly deg 2) R-squared score (training): {:.3f}'
     .format(linreg.score(X_train, y_train)))
print('(poly deg 2) R-squared score (test): {:.3f}\n'
     .format(linreg.score(X_test, y_test)))

print('\nAddition of many polynomial features often leads to\n\
overfitting, so we often use polynomial features in combination\n\
with regression that has a regularization penalty, like ridge\n\
regression.\n')

X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,
                                                   random_state = 0)
linreg = Ridge().fit(X_train, y_train)

print('(poly deg 2 + ridge) linear model coeff (w):\n{}'
     .format(linreg.coef_))
print('(poly deg 2 + ridge) linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('(poly deg 2 + ridge) R-squared score (training): {:.3f}'
     .format(linreg.score(X_train, y_train)))
print('(poly deg 2 + ridge) R-squared score (test): {:.3f}'
     .format(linreg.score(X_test, y_test)))

print ("=="*40)
print("Test Data")
print(X_test)

x_test   =  pd.read_csv (DataPath+'TestData_Predictors.csv')
print ("=="*40)
print ("Real Test Data")
print (x_test.values)

Test_F1_poly = poly.fit_transform(x_test.values)
print (Test_F1_poly)

#
# #np.reshape(np.array(DF['Brain']),(-1,1))
# X_test   = x_test.values
# print ("=="*40)
# print ("Formatted Test Data")
# print (X_test)


# Sample = np.array(x_test)
# print ('Sample')
# print (Sample)
#
# Reshaped = np.reshape (Sample,(1,-1))
# print ("Reshaped")
# print (Reshaped)


Predictions = linreg.predict(Test_F1_poly)
print ("=="*40)
print ("Predictions")
print (Predictions)
