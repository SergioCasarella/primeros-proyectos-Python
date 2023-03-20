import numpy as np

'''
La libreria NumPy permite obtener los valores maximo, minimo y promedio de las matrices en python
'''

matriz1 = np.array([[1,0,0],
                   [1,2,0],
                   [1,2,3]
                   ])

print('Max:',np.max(matriz1))

print('Min:',np.min(matriz1))

print('averange:',np.average(matriz1))