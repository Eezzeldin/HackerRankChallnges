
'''
F, N = map(int, input().split())
print (F,N)
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)
print (train)
print (test)
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

F, N = map(int, input().split())
#print (F,N)
inputData = [input().split() for _ in range (N)]
#print ("=="*40)
#print ("InputData",'\n')
#print (inputData)
#for line in inputData :
#    for number in line :
#        number = float(number)
#print (inputData,'\n')

Training = [[float (number) for number in line] for line in inputData ]
#print ("Training")
#print (Training,'\n')
Training = np.array (Training)
#print ("Numpy Training")
#print (Training, '\n')

T         = int(input())
inputData = [input().split() for _ in range (T)]
Test      = np.array([[float (number) for number in line] for line in inputData ])
#print ("Test")
#print (Test,'\n')

Predictors= Training [:,0:F]
#print ('Predictors')
#print (Predictors,'\n')
Responce =  Training [:,2]
#print ('Responce')
#print (Responce , '\n')

poly = PolynomialFeatures(degree=2)
Predictors_poly = poly.fit_transform(Predictors)
X_train, X_test, y_train, y_test = train_test_split(Predictors_poly, Responce,random_state = 0)
#print ('X_train')
#print (X_train , '\n')
#print ('X_test')
#print (X_test , '\n')
#print ('y_train')
#print (y_train , '\n')
#print ('y_test')
#print (y_test, '\n')
linreg   = LinearRegression().fit(X_train, y_train)

NewData_Poly= poly.fit_transform(Test)
Predictions= linreg.predict(NewData_Poly)
for prediction in Predictions:
    print (prediction)


'''
import numpy as np
from sklearn import linear_model as lm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)
model = Pipeline([('poly', PolynomialFeatures(degree=3,include_bias=False)),
                  ('linear', lm.LinearRegression())])
model = model.fit(train[:,range(F)],train[:,[F]])
ymod=model.predict(test)
print(*np.round(ymod.ravel(),2),sep='\n')
'''
