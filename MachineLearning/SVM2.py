from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import sklearn.preprocessing as preprocessing

digits = load_digits()
digits_data = digits.data

x_train,x_test, y_train, y_test = train_test_split(digits.data,digits.target,stratify= digits.target,random_state = 30)

print(x_train.shape)
print(x_test.shape)

svm_classifier = SVC()
svm_clf = svm_classifier.fit(x_train,y_train)
print(svm_clf.score(x_test,y_test))

standardizer = preprocessing.StandardScaler()
standardizer = standardizer.fit(digits_data)
digits_standardized = standardizer.transform(digits_data)


x_train,x_test,y_train,y_test = train_test_split(digits_standardized,digits.target,stratify = digits.target,random_state = 30)

svm_classifier2 = SVC()
svm_clf2 = svm_classifier2.fit(x_train,y_train)
print(svm_clf2.score(x_test,y_test))






