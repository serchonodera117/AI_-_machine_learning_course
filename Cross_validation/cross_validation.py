# -*- coding: utf-8 -*-
"""Cross_validation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uA3dTADhPj8hIQT9-3630Vy1yeDfpPhu
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#used technique: random forest clasifier
people = pd.read_csv("salario.csv")

myForest = RandomForestClassifier()
myForest.fit(people[["edad", "estudio"]].values,
             people["ingreso"].values)

print(myForest.score(people[["edad", "estudio"]].values, people["ingreso"].values))

print(cross_val_score(myForest, people[["edad", "estudio"]].values,
                                               people["ingreso"].values,
                                               cv = 5).mean())