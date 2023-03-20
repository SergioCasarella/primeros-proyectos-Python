import numpy as np

'''
* Cómo dividir uniformemente un rango de numeros en python usando numpy

Hay muchas situaciones en las que tienes un rango de numeros y te gustaria dividir por igual ese ango de numeros en intervalos. El metodo linspace de NumPy esta diseñado para resolver este problema. Linspace tiene tres argumentos:
- El inicio del intervalo.
- El fin del intervalo.
- El numero de subintervalos en los que deseas que se divida el intervalo.
'''

intervalo1 = np.linspace(0, 12, 7)
print(intervalo1)
print()

intervalo2 = np.linspace(0,10,6)
print(intervalo2)
print()

intervalo3 = np.linspace(0,12,7)
print(intervalo3)