from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np 

np.random.seed(100)
boston = load_boston()

x_train,x_test, y_train, y_test = train_test_split(boston.data,boston.target,random_state = 30)
print(x_train.shape)
print(x_test.shape)

rf_reg = RandomForestRegressor()
rf_reg = rf_reg.fit(x_train, y_train) 

print(rf_reg.score(x_train,y_train))
print(rf_reg.score(x_test,y_test))

y_pred = rf_reg.predict(x_test[0:2])
print(y_pred)
d = {}
accuracy = []
for i in range(3,6):
    rf_regress = RandomForestRegressor(n_estimators = 50,max_depth = i)
    rf_regress2 = RandomForestRegressor(n_estimators = 100,max_depth = i)
    rf_regress3 = RandomForestRegressor(n_estimators = 200,max_depth = i)
    first = [i,50]
    second = [i,100]
    third = [i,200]
    rf_fit = rf_regress.fit(x_train,y_train)
    rf_fit2 = rf_regress2.fit(x_train,y_train)
    rf_fit3 = rf_regress3.fit(x_train,y_train)
    rf_accuracy = rf_fit.score(x_test,y_test)
    rf_accuracy2 = rf_fit2.score(x_test,y_test)
    rf_accuracy3 = rf_fit3.score(x_test,y_test)
    first1 = tuple(first)
    second1 = tuple(second)
    third1 = tuple(third)
    d[first1] = rf_accuracy
    d[second1] = rf_accuracy2
    d[third1] = rf_accuracy3
print(d)  
max_value = max(d,key=d.get)
print(max_value)



