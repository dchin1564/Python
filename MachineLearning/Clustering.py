from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
import sklearn.preprocessing as preprocessing
from sklearn import metrics

iris = load_iris()
iris_data = iris.data
y = iris.target
km_cls = KMeans(n_clusters = 3)
km_cls.fit(iris_data)
print(metrics.homogeneity_score(y,km_cls.labels_))

agg_cls = AgglomerativeClustering(n_clusters = 3)
agg_cls.fit(iris.data)
print(metrics.homogeneity_score(y,agg_cls.labels_))

af_cls = AffinityPropagation()
af_cls.fit(iris.data)
print(metrics.homogeneity_score(y,af_cls.labels_))

