import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
iris = load_iris()
x= iris.data
kmeans = KMeans(n_clusters=3)
kmeans.fit(x)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
for i in range(3):
    cluster_points =x[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1])
plt.scatter(centers[:, 0], centers[:, 1,], c='red', s=200, marker='x')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()
plt.title('K-means Clustering')
plt.show()