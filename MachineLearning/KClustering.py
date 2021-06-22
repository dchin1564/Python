import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
#.data is where our features are and scale brings the values of the data to between -1 and 1 b/c the values are large
data = scale(digits.data)
#.target gets the labels
y = digits.target
print(digits)
print(y)
k = 10
samples, features = data.shape

def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
            #scores compare the digits.target to the estimator labels 
            #unsupervised training so KMeansClustering automatically generates a y value for each test data point that we give it
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))

#n_clusters is pretty much the amount of centroids you want to use
#init is used to know where to place the centroids in relation to one another
#n_init is the amount of times the algorithm is going to run
clf = KMeans(n_clusters=k, init="k-means++", n_init=10)
bench_k_means(clf, "1", data)