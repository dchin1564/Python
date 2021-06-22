import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
import matplotlib.pyplot as plt
from matplotlib import style 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

dataset = pd.read_csv('car.txt')
#print(dataset)

#changes text values into integer values
label = preprocessing.LabelEncoder()
buying = label.fit_transform(list(dataset['buying']))
maint = label.fit_transform(list(dataset['maint']))
door = label.fit_transform(list(dataset['door']))
persons = label.fit_transform(list(dataset['persons']))
lug_boot = label.fit_transform(list(dataset['lug_boot']))
cls = label.fit_transform(list(dataset['class']))

predict = 'class'
x = list(zip(buying,maint,door,persons,lug_boot))
y = list(cls)
x_train , x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1)
k = 5

model = KNeighborsClassifier(n_neighbors = k)
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
print("Test set accuracy: ", accuracy_score(y_test,y_predict))
acc = model.score(x_test,y_test)
print("Accuracy score:" , acc)










