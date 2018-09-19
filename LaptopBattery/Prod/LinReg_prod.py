from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
np.set_printoptions(precision=2)


Laptop   = pd.read_table ('../Data/trainingdata.txt',sep =',',header = None, names =      ['Predictor','Responce'])
Laptop ['Predictor'] = Laptop ['Predictor'].apply (lambda x : float (x))
Laptop ['Responce']  = Laptop ['Responce'].apply (lambda x : float (x))
Laptop   = Laptop [Laptop ['Responce'] < 8]
print (Laptop)




X_R1 = (np.array (Laptop ['Predictor']).reshape (-1,1))
y_R1 = (np.array (Laptop ['Responce']).reshape (-1,1))

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)
linreg = LinearRegression().fit(X_train, y_train)

# print('linear model coeff (w): {}'
#      .format(linreg.coef_))
# print('linear model intercept (b): {:.3f}'
#      .format(linreg.intercept_))
# print('R-squared score (training): {:.3f}'
#      .format(linreg.score(X_train, y_train)))
# print('R-squared score (test): {:.3f}'
#      .format(linreg.score(X_test, y_test)))

NewData     = 0.09
Predictions = linreg.predict(NewData)
print (Predictions)
