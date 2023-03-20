import numpy as np

'''
* Cómo obtener un rango de numeros en python utilizando NumPy

NumPy tiene un metodo llamado arange que toma dos numeros y devuelve un arreglo de numeros enteros que son mayores o iguales a el primer numero y menores que el segundo numero
'''
mi_arange = np.arange(0,5)
print(mi_arange)

'''Tambien puedes incluir una tercera variable en el metodo arange que proporciona un tamaño de paso para que la funcion regrese. Pasar 2 como tercera variable devolvera cada segundo numero en el rango, pasar 5 como tercera variable devolvera cada quinto numero en el rango, y asi sucesivamente:'''

mi_arange2 = np.arange(1,11,2)
print(mi_arange2)

mi_arange3 = np.arange(0,10,3)
print(mi_arange3)