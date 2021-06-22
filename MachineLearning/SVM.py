import sklearn 
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

cancer_data = datasets.load_breast_cancer()

x = cancer_data.data 
y = cancer_data.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3)

clf = svm.SVC(kernel = 'rbf')
clf.fit(x_train,y_train)

y_prediction = clf.predict(x_test)
print("Test Accuracy: ", metrics.accuracy_score(y_test,y_prediction))