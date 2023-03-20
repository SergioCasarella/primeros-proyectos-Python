import numpy as np

'''
Suma

Al sumar un solo numero a un arreglo de Numpy, ese numero se suma a cada elemento en el arreglo.
'''

arreglo = np.array([1,2,3,4,5])

print(2 + arreglo)

'''
Puedes sumar dos arreglos NumPy usando el operador +. Los arreglos se suman elemente por elemento (lo que significa que los primeros elementos se suman entre si, los segundos elementos se suman entre si, y asi sucesivamente).
'''

print(arreglo + arreglo)

arreglo2 = np.random.randint(1,21, size=(2,10))
arreglo3 = np.random.randint(1,21, size=(2,10))

print()
print(arreglo2)
print()
print(arreglo3)

print()
print(arreglo2 + arreglo3)