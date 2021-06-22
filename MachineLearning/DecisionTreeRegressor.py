from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np
np.random.seed(100)
boston = load_boston()

x_train,x_test, y_train, y_test = train_test_split(boston.data,boston.target,random_state = 30)
print(x_train.shape)
print(x_test.shape)

dt = DecisionTreeRegressor()
dt_reg = dt.fit(x_train,y_train)

print(dt_reg.score(x_train,y_train))
print(dt_reg.score(x_test,y_test))

y_pred = dt.predict(x_test[0:2])
print(y_pred)
accuracy = {}
for i in range(2,6):
    dt_regress = DecisionTreeRegressor(max_depth = i)
    dt_fit = dt_regress.fit(x_train,y_train)
    dt_accuracy = dt_fit.score(x_test,y_test)
    accuracy[i] = dt_accuracy

print(accuracy)
max_value = max(accuracy,key=accuracy.get)
print(max_value)


