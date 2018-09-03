import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
np.set_printoptions(precision=2)

from sklearn.datasets import make_friedman1
X_F1, y_F1 = make_friedman1(n_samples = 100,
                            n_features = 7, random_state=0)

poly = PolynomialFeatures(degree=2)
X_F1_poly = poly.fit_transform(X_F1)

X_train, X_test, y_train, y_test = train_test_split(X_F1_poly, y_F1,
                                                   random_state = 0)
linreg   = LinearRegression().fit(X_train, y_train)
coef     = linreg.coef_
intercept= linreg.intercept_
trainScore=linreg.score(X_train, y_train))
testScore=linreg.score(X_test, y_test))

                                                   
