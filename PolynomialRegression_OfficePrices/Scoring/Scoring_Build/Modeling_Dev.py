import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

np.set_printoptions(precision=2)


def PolyPredict (NewData,Degree):
    DataPath = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/Modeling/Data/'
    X_F1  =  pd.read_csv (DataPath+'TrainingData_Predictors.csv').values
    Y_F1  =  pd.read_csv (DataPath+ 'TrainingData_Responce.csv')
    y_F1  = Y_F1 ['Responce'].values

    poly = PolynomialFeatures(degree=Degree)
    X_F1_poly = poly.fit_transform(X_F1)
    X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,random_state = 0)
    linreg   = LinearRegression().fit(X_train, y_train)

    NewData_Poly= poly.fit_transform(NewData.values)
    Predictions= linreg.predict(NewData_Poly)
    return Predictions

if __name__ == "__main__":
    DataPath = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/Modeling/Data/'
    NewData= pd.read_csv (DataPath+ 'TestData_Predictors.csv')
    Predictions = PolyPredict (NewData,2)
    # print ("=="*40)
    # print ("Predictions")
    # print (Predictions)
