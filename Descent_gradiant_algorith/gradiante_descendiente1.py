#linear regresion with descendant gradiant
import numpy as np 
import matplotlib.pyplot as plt
import sympy as symp
from sklearn.linear_model import LinearRegression

#independent variable
experience = np.array([[5],[6],[13]])

#objective variable
salary = np.array([6.85, 16.83, 26.84])

#Linear model created with minimun quadratic methods
myModel = LinearRegression().fit(experience.reshape(3,-1),salary)

#previzualization
print("Insercion with Y axis (n): %0.2f"%myModel.intercept_)
print("pendiente (m): %0.2f"%myModel.coef_[0])
print("suma de cuadrados de los residuos (RSS): %0-2f"%((salary-myModel.predict(experience))**2).sum())

plt.figure(figsize=(8,6))

plt.scatter(experience, salary, color="gold", s=250, marker="o", label="Valor verdadero")

plt.scatter(experience, myModel.predict(experience), color="blue", s=250, marker="p", label="valor predicho")

plt.plot(experience, myModel.predict(experience), linewidth=4, color="deepink", label="Modelo lineal")
experience = experience.reshape(3)

plt.ylabel("salarios de miels de pesos ($)", size=16)
plt.xlabel("Años de experiencia", size = 16)
plt.legend(bbox_to_anchor=(1.3,0.5))
plt.grid()
plt.box(False)
plt.show()