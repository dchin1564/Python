#Write your code here
from sklearn.datasets import load_iris
import sklearn.preprocessing as preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer
import numpy as np 
iris = load_iris()
iris_data = iris.data
normalized = preprocessing.Normalizer(norm='l2').fit(iris.data)
iris_normalized = normalized.transform(iris.data)
print(iris_normalized.mean(axis=0))

reshaper = iris.target.reshape(-1,1)
onehotencoder = preprocessing.OneHotEncoder()

iris_target_onehot = onehotencoder.fit_transform(reshaper)
print(iris_target_onehot.toarray()[[0,50,100]])


iris_data[:50,:] = np.nan

imputer = preprocessing.Imputer(missing_values='NaN', strategy ='mean')
imputer = imputer.fit(iris_data)
iris_imputed = imputer.transform(iris_data)
print(iris_imputed.mean(axis=0))
