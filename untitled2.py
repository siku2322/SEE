# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y8_Y4b5pTJ8sHiSSJJQ2CDSkW2-jvtCR
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('/content/Mall_Customers.csv')
data.info()
data.shape
data.describe()
data.isnull().sum()
x = data.iloc[:, [3, 4]]

wcss_list = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss_list)
plt.xlabel('no of clusters')
plt.ylabel('wcss_list')
plt.grid(True)
plt.show()

optimal_clusters = 5
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(x)

plt.scatter(x.iloc[y_predict == 0, 0], x.iloc[y_predict == 0, 1], s=100, c='blue', label='cluster 1')
plt.scatter(x.iloc[y_predict == 1, 0], x.iloc[y_predict == 1, 1], s=100, c='pink', label='cluster 2')
plt.scatter(x.iloc[y_predict == 2, 0], x.iloc[y_predict == 2, 1], s=100, c='green', label='cluster 3')
plt.scatter(x.iloc[y_predict == 3, 0], x.iloc[y_predict == 3, 1], s=100, c='orange', label='cluster 4')
plt.scatter(x.iloc[y_predict == 4, 0], x.iloc[y_predict == 4, 1], s=100, c='magenta', label='cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='centroids')
plt.title('customer segments')
plt.xlabel('annual income')
plt.ylabel('spending score')
plt.legend()
plt.show()