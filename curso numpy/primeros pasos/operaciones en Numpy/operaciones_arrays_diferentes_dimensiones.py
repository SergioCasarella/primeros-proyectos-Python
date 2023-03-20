import numpy as np

'''
Es una caractetistica avanzada de NumPy para realizar operaciones aritmeticas con arrays de distintas dimensiones, elemento a elemento utilizando los simbolos matematicos (+,-,*,/,//,**).
Estas operaciones son posibles cuando el array resultando tiene la misma dimension que al menos uno de los arrays operandos.

En el ejemplo siguiente el array a tiene 3 elementos por fila que coincide con el numero de elementos del array b. Numpy para realizar el calculo suma cada fila de a con los elementos de b, elemento a elemento.
'''

a = np.ones((3,3))
b = np.array([1,2,3])
c = a + b

print(a)
print()

print(b)
print()

print(a + b)
print()

'''
En el ejemplo siguiente el array a tiene 3 elementos por columna que coincide con los elementos del array b. Numpy para realizar el calculo suma cada column de a con los elementos b, elemento a elemento.
'''

a1 = np.ones((3,3))
b1 = np.array([[5],[10],[15]])
c1 = (a1 + b1)

print(c1)

