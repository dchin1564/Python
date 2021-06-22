from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
iris_data = iris.data

x_train,x_test, y_train, y_test = train_test_split(iris.data,iris.target,stratify= iris.target,random_state = 30)

print(x_train.shape)
print(x_test.shape)

knn_classifier = KNeighborsClassifier()
knn_clf = knn_classifier.fit(x_train,y_train)

print(knn_clf.score(x_train,y_train))
print(knn_clf.score(x_test,y_test))

accuracy_values = {}
for i in range(3,11):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn_fit = knn.fit(x_train,y_train)
    knn_accuracy = knn_fit.score(x_test,y_test)
    accuracy_values[i] = knn_accuracy

print(accuracy_values)
max_value = max(accuracy_values,key=accuracy_values.get)
print(max_value)