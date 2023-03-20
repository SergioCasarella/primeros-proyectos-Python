import numpy as np

'''¿Cómo crear un arreglo de identidad en Python usando NumPy

Cualquiera que hay estudiado algebra lineal estara familiarizado con el concepto de un 'arreglo identidad', que es un arreglo cuadrado cuyos valores diagonales son 1. NumPy tiene una funcion incorporada que incluye un argumento para contruir matrices de identidad. La funcion es 'eye'.'''

miIdentidad2 = np.identity(2)
print('Matriz Identidad 2x2')
print(miIdentidad2)
print()

miIdentidad3 = np.identity(3)
print('Matriz Identidad 3x3')
print(miIdentidad3)

miIdentidad4 = np.identity(4)
print('Matriz identidad 4x4')
print(miIdentidad4)