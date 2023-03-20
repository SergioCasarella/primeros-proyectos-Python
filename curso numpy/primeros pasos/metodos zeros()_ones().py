import numpy as np

'''Como generar uno y ceros en python con NumPy

Mientras programas, de vez en cuando necesitara crear arreglos de unos o ceros. NumPy tiene metodos incorporados que te permiten hacer ambas cosas. 
Podemos crear arreglos de ceros utilizando zeros de NumPy. Le pasas el numero de enteros que quisieras crear como el argumento de la funcion:
'''
mis_zeros = np.zeros(10)
print(mis_zeros)

'''
Tambien puedes hacer algo similar utilizando matrices tridimensionales. Por ejemplo, np.zeros(5, 5) crea un arreglo de 5x5 que contiene to0dos ceros.
'''
mis_zeros2 = np.zeros((3,2))
print(mis_zeros2)

'''
Podemos crear arreglos de unos usando un metodo similar llamado 'ones'.'''

mis_unos = np.ones(5)
print(mis_unos)

mis_unos2 = np.ones((2,2))
print(mis_unos2)