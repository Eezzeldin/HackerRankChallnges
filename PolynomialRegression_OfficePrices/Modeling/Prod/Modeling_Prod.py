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
