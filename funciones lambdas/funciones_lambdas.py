'''Qué son las funciones lambda en python

En python, las funciones lambda son tambien conocidas
como funciones anonimas porque se definen sin un nombre

Como sabes, una funcion en Python se define con la palabra reservada def. Sin embargo, una funcion anonima se define con la palabra reservada lambda.

Cómo se define una funcion anonima en Python

La sintaxis para definir una funcion lambda es la siguiente:


lambda parametros: expresion


caracteristicas principales de una funcion anonima:

* Son funciones que puden definir cualquier numero de parametros pero una unica expresion. Esta expresion es
evaluada y devuelta.

* Se pueden usar en cualquier lugar en el que la funcion sea requerida.

* Se suelen usar en combinacion con otras funciones,
generalmente como argumento de otra funcion.

ejemplo:
'''
cuadrado = lambda x: x * 2
print(cuadrado(3))

'''Como ves, la funcion no tiene nombre y toda la definicion devuelve
una funcion que se asigna al identificador cuadrado.

En el siguiente ejemplo se aprecian las similitudes y diferencias
usar una funcion anonima y una funcion normal:
'''
def cuadrado1(x):
    return x ** 2

cuadrado2 = lambda x: x**2

'''Vamos a descubrir el potencial de las funciones lambda,
especialmente cuando se usan en combinacion con otras
funciones

La funcion map() en Python aplica una funcion a cada uno de
los elementos de una lista.

map(una_funcion, una_lista)

Imagina que tienes una lista de enteros y quieres obtener
una lista con el cuadrado de cada uno de ellos.
'''
enteros = [1,2,4,7]
enteros1 = [x**2 for x in enteros]
print(enteros1)

'''Sin embargo, podemos usar una funcion anonima en combinacion
con map() para obtener el mismo resultado de una manera mucho
mas simple:
'''

cuadrados = list(map(lambda x: x**2, enteros))
print(cuadrados)

cuadrados3 = list(map(cuadrado2, enteros))
print(cuadrados3)

'''La cosa se vuelve todavia mas interesante cuando, en lugar de
una lista de valores, pasamos como segundo parametro una lista
de funciones:
'''

enteros = [1,2,4,7]

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

funciones = [cuadrado, cubo]

for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)




















