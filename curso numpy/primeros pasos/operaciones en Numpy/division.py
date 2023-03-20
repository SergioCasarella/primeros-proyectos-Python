import numpy as np

'''
División
En este punto, probablemente no te sorprende saber que la división en arreglos NumPy se realiza elemento por elemento. Un ejemplo de división de arr por un sólo número se ve a continuación:

arr / 2

#Devuelve array([0. , 0.5, 1. , 1.5])
La división tiene una excepción notable en comparación con las otras operaciones matemáticas que hemos visto en esta sección. Dado que no podemos dividir por cero, al hacerlo, el campo correspondiente se completará con un valor nan, que es la abreviatura de Python para "No es un número" (“Not A Number”). Jupyter Notebook también imprimirá una advertencia similar a esta:

RuntimeWarning: invalid value encountered in true_divide
Un ejemplo de dividir por cero es con un arreglo NumPy que se muestra a continuación.

arr / arr

#Devuelve array([nan,  1.,  1.,  1.])
Aprenderemos cómo tratar los valores nan con más detalle más adelante en este curso.
'''