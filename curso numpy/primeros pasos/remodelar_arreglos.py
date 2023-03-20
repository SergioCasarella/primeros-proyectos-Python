import numpy as np

'''
Es muy comun tomar un arreglo con ciertas dimensiones y transformar ese arreglo en una forma diferente. Por ejemplo, es posible que tengas un arreglo unidimensional con 10 elementos y desees cambiarlo a un arreglo bidimensional de 2x5.
'''

array_comun = [1,2,3,4,5,6]

array_numpy = np.array(array_comun)

array_modificado = array_numpy.reshape(3,2)

print(array_modificado)

print()

aleatorio = np.random.randint(0,10,10)

print(aleatorio)

nueva_forma = aleatorio.reshape(2,5)

print(nueva_forma)

'''
Ten en cuanta que para usar el metodo reshape, el arreglo original debe tener la misma cantidad de elementos que el arreglo en el que estas tratando de remodelarlo.

Si tienes curiosidad sobre la forma actual de un arreglo NumPy, puede determinar su forma utilizando el atributo shape de Numpy. Usando nuestra estructura de la variable anterior, a continuacion se muestra un ejemplo de como llamar al atributo shape:
'''