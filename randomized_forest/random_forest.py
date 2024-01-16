# -*- coding: utf-8 -*-
"""random_forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYPfvnAIcDhfJ3gOfsgbMOQ_-r-iCG4V
"""

#showing with replace
import pandas as pd

people = pd.read_csv("ingresos.csv")

print(people.sample(frac=2/3, replace=True))

#Randomozed, selection of features for divide, max_features= sqrt(num_features)
from random import sample

print(people.columns[:-1])
print(sample(set(people.columns[:-1]), 3)) #randomized selection of sets from a group of data, is highly recomended to chose quadratic root from the number of features.

from sklearn.ensemble import RandomForestClassifier

#(number_of_trees, criterion{entropy or gini},)
myForest = RandomForestClassifier(n_estimators=100,
                                  criterion= "gini",
                                  max_features="sqrt",
                                  bootstrap=True,
                                  max_samples=2/3,
                                  oob_score=True)

myForest.fit(people[people.columns[:-1]].values, people["ingreso"].values)

print(myForest.predict([[50,16,1,1,40]]))
print("Accuracy: ", myForest.score(people[people.columns[:-1]].values, people["ingreso"].values))

print("Out of back: ",myForest.oob_score_)#out of back, to test data that wasn't used to train trees, data that stayed out of metrics

#view of randimized forest
import matplotlib.pyplot as plt
from sklearn import tree

for arbol in myForest.estimators_:
  tree.plot_tree(arbol, feature_names=people.columns[:-1])
  plt.show()