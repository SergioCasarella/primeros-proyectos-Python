import numpy as np

'''
La multiplicacion tambien se realiza elemento por elemento tanto para casos de un solo numero como para casos de operaciones entre arreglos de numpy
'''

arreglo = np.array([2,3,4,5,6,7,8])

print(6 * arreglo)

arreglo2 = np.random.randint(0,10,7)

print('arreglo 1:')
print(arreglo)
print()

print('arreglo 2:')
print(arreglo2)
print()
print('multiplicacion:')
print(arreglo * arreglo2)