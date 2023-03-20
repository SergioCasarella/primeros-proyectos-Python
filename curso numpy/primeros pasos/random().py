import numpy as np

'''
NumPy tiene varios metodos integrados que te permiten crear matrices de numeros aleatorios. Cada uno de estos metodos comienza con 'random'. A continuacion se muestran algunos ejemplos:

Primera vamos a empezar por ver como generar uno o varios enteros, para ellos llamaremos al modulo .random de la libreria numpy seguido de la funcion .randint() indicandole entre parentesis un numero que sera el numero maximo que queremos que salga, si le indicadmos el numero 10 nos devolvera un numero aleatorio entre el 0 y el 10, si le indicamos el 20 pues un numero aleatorio entre el 0 y el 20.
'''
aleatorio = np.random.randint(10)

print(aleatorio)

'''
Si en lugar de un solo numero queremos que nos genere un array con varios numeros tendremos que poner una coma despues del numero que indica el rango maximo en el caso del ejemplo seria el 10 y a continuacion la palabra 'size=()' y entre parentesis el numero de elementos que queremos que genere.
'''
lista_aleatorios = np.random.randint(10, size=(5))
lista_aleatorios2 = np.random.randint(100, size=(10))

print(lista_aleatorios)
print(lista_aleatorios2)

'''
Esto seria para una matriz de 1 dimension pero ¿Cómo hariamos si queremos que nos genere una matriz de varias dimensiones? Pues tan solo tenemos que indicar en los parentesis size() las dimensiones que queremos que tenga la matriz con los numeros aleatorios.
'''

matriz_aleatoria1 = np.random.randint(10, size=(4, 2))
print(matriz_aleatoria1)

matriz_aleatoria2 = np.random.randint(100, size=(50,2))
print(matriz_aleatoria2)

'''
Numeros decimales aleatorios

¿Y si no queremos que sea de numeros enteros? Pues tambien podemos generar matrices de numeros decimales mas precisos. Lo haremos con la funcion .rand() pero esta vez entre los parentesis no indicaremos el rango de los numeros, indicaremos el numero de los elementos que queremos que tenga el array. Hay que tener en cuenta que esta funcion devolvera numeros aleatorios entre el 0 y el 1.
'''
aleatorio_decimal = np.random.rand(5)
print(aleatorio_decimal)

aleatorio_decimal2 = np.random.rand(3)
print(aleatorio_decimal2)

'''
Si queremos indicar una matriz de varias dimensiones con numeros decimales tan solo tendremos que indicar el numero de filas y columnas entre los parentesis de .rand()
'''

matriz_decimales1 = np.random.rand(3,3)
print(matriz_decimales1)

matriz_decimales2 = np.random.rand(2,2)
print(matriz_decimales2)

'''
Numeros aleatorios indicandole varios numeros para elegir

Otra funcion muy util de la libreria NumPy es la funcion .choice(), a esta funcion le pasaremos un array con varios numeros de los cuales elegira uno de forma aleatoria.
'''

eleccion_aleatoria = np.random.choice([4,6,7,8,3,2,18,65,43,90,45,100])
print(eleccion_aleatoria)
eleccion_aleatoria2 = np.random.choice([5,6,7,3])
print(eleccion_aleatoria2)

print()

numeros_aleatorios = np.random.randint(10, size=(5))

print(numeros_aleatorios)

eleccion_aleatoria3 = np.random.choice(numeros_aleatorios)

print(eleccion_aleatoria3)

'''
Si queremos que nos genere una matriz de varias dimensiones con numeros aleatorios de este array indicado lo haremos con size=() y entre los parentesis el numeros de filas y columnas.
'''

matriz_choice = np.random.choice([4,7,9,1],size=(2,2))
print(matriz_choice)
print()

numeros_aleatorios2 = np.random.randint(50, size=(8))
print(numeros_aleatorios2)

matriz_aleatoria3 = np.random.choice(numeros_aleatorios2, size=(4,2))
print(matriz_aleatoria3)








