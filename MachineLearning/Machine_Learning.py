import pandas as pd
import numpy as np 
import sklearn 
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import style 
"""
df = pd.read_csv('iris.data')
print(df.head())

label = preprocessing.LabelEncoder()
sepal_length = label.fit_transform(list(df['sepallength']))
sepal_width = label.fit_transform(list(df['sepalwidth']))
petal_length = label.fit_transform(list(df['petallength']))
petal_width = label.fit_transform(list(df['petalwidth']))
cls = label.fit_transform(list(df['class']))

x = list(zip(sepal_length,sepal_width,petal_length,petal_width))
y = list(cls)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.8)
k=8
model = KNeighborsClassifier(n_neighbors = k)

model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print("Accuracy Score: ", accuracy_score(y_test,y_predict))
"""
"""
df = pd.read_csv('adult.data')
label = preprocessing.LabelEncoder()
age = label.fit_transform(list(df['age']))
workclass = label.fit_transform(list(df['workclass']))
fnlwgt = label.fit_transform(list(df['fnlwgt']))
education = label.fit_transform(list(df['education']))
education_num = label.fit_transform(list(df['education-num']))
marital_status = label.fit_transform(list(df['marital-status']))
occupation = label.fit_transform(list(df['occupation']))
relationship = label.fit_transform(list(df['relationship']))
race = label.fit_transform(list(df['race']))
sex = label.fit_transform(list(df['sex']))
capital_gain = label.fit_transform(list(df['capital-gain']))
capital_loss = label.fit_transform(list(df['capital-loss']))
hours_per_week = label.fit_transform(list(df['hours-per-week']))
native_country = label.fit_transform(list(df['native-country']))
salary = label.fit_transform(list(df['salary']))

x = list(zip(age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country))
y = list(salary)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
print("Decision Tree score: ", accuracy_score(y_test,y_predict))
"""
"""
k = 10
model = KNeighborsClassifier(n_neighbors = k)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print("Accuracy Score: " , accuracy_score(y_test,y_predict))
"""

df = pd.read_csv("wine.data")

x = df.drop(columns = ['quantity'])
y = df['quantity']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)

model = linear_model.LinearRegression()
model.fit(x_train,y_train)
y_prediction = model.predict(x_test)
#print("Mean squared error score: ", mean_squared_error(y_test,y_prediction))
acc = model.score(x_test,y_test)
#print(acc)
print("intercept ", model.intercept_)
print("coefficient ", model.coef_[0])
#plt.scatter(x_train.malic_acid,y_train,color = "blue")
plt.plot(x_train,model.coef_[1]*x_train + model.intercept_,'-r')
plt.show()
