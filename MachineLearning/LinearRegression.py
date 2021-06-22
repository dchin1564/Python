import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from matplotlib import style 


df = pd.read_csv('student-mat.csv',sep = ';')
#print(df)
print(df.shape)

#print(df.values)

#shows statistical data
#print(df.describe())

#take a look at the dataset
#print(df.head())

df = df[['G1','G2','G3','studytime','failures','absences']]


predict = 'G3'

X = np.array(df.drop([predict], 1))

y = np.array(df[predict])

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size = 0.)
model = linear_model.LinearRegression()
model.fit(X_train,y_train)

prediction = model.predict(X_test)
print("Coefficients: ", model.coef_)
print("Mean Squared Error: ", mean_squared_error(y_test,prediction))
acc = model.score(X_test,y_test)
print(acc)




plt.scatter(X_train,y_train,color = 'blue')

plt.show()











