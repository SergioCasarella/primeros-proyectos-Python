'''
¿Qué son los arreglos de NumPy?

Los arreglos de NumPy son la forma principal de almacenar datos utilizando la biblioteca NumPy. Son similares a ls listas normales de python, pero tienen la ventaja de ser mas rapidas y tener mas metodos integrados.

Los arreglos de NumPy son creados llamando al metodo array() de la libreria. Dentro del metodo, deberias pasar una lista.

ejemplo:'''

import numpy as np

lista_ejemplo = [1,2,3]

lista_Numpy = np.array(lista_ejemplo)

print(type(lista_Numpy))

'''
Los dos tipos diferentes de arreglos de NumPy

Hay dos tipos diferentes de arreglos de NumPy: vectores y matrices.

Los vectores son arreglos de NumPy uni-dimensionales y se ven asi:

* mi_vector = np.array(['este','es','un','vector'])

Las matrices son arreglos bi-dimensionales y son creadas pasando lista de lista dentro del meetodo np.array(). ejemplo:

mi_matriz = [[1,2,3],[4,5,6],[7,8,9]]

np.array(mi_matriz)

Tambien puedes expandir los arreglos de NumPy para trabajar con matrices de tres, cuatro, cinco, seis o mas dimensiones, pero son raras y estan en gran parte fuera del alcance de este curso.
'''



