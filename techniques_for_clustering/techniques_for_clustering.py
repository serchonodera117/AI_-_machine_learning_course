# -*- coding: utf-8 -*-
"""techniques_for_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l1rnmmqsPeqCbYe3BkqbyyDYHHCEq3-6
"""

#chebyshev distances
import numpy as np
import matplotlib.pyplot as plt

#load data
myData = np.loadtxt("venta_propiedades.csv", delimiter=",")

#graphic of data
plt.figure(figsize=(6,6))
plt.scatter(myData[:,0], myData[:,1],
            c=np.linspace(0,1, myData.shape[0]), s=300, alpha=0.6)
plt.xlabel("Antiquity of building in years", fontsize=14)
plt.ylabel("House price in pesos (1:100,000)", fontsize=14)
plt.box(False)
plt.show()

from sklearn.cluster import DBSCAN

#load data
mydata = np.loadtxt("venta_propiedades.csv", delimiter=",")

#identify cluster with diferent distances
distances = ["euclidean", "chebyshev", "manhattan"]

fig = plt.figure(figsize=(12,4))
plt.set_cmap("plasma")
for d in range (len(distances)):
  clusters = DBSCAN(2, min_samples=10,
                    metric=distances[d]).fit_predict(mydata)
  ax = fig.add_subplot(1,3,d+1)

  #points considers noise
  ax.scatter(mydata[clusters==-1][:,0], mydata[clusters==-1][:,1],
             c="lightgray", s=200, marker=2)

  #points belonging to clusters
  ax.scatter(mydata[clusters>=0][:,0], mydata[clusters>=0][:,1],
             c=clusters[clusters>=0], s=200,
             linewidth=0.5, edgecolors="black")
  ax.set_title(distances[d].capitalize(), fontsize=24)
  ax.axis("off")

plt.show()