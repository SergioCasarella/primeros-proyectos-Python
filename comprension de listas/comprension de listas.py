#Comprension de listas

'''La comprension de listas en Python es un metodo
sintactico para crear listas (y otras colecciones)
a partir de elementos de otras listas (o colecciones)
de una forma rapida de escribir, muy legible y
funcionalmente eficiente.'''

lenguajes = ['python','c','c++','java']

'''Usando comprension de listas, podemos crear
una nueva lista con las mismas cadenas pero con
su primera letra en mayuscula (es decir, aplicar
el metodo capitalize() de las cadenas).'''

mayusculas = [lenguaje.capitalize() for lenguaje in lenguajes]

print(mayusculas)

'''funcionalmente similar a lo siguiente:'''

mayusculas1 = []

for lenguaje in lenguajes:
    mayusculas1.append(lenguaje.capitalize())

print(mayusculas1)


'''Consideremos esta lista de numeros:'''

numeros = [1,2,3,4,5]

'''vamos a crear una nueva lista 'doble' que
contenga el doble de cada uno de los numeros de
numeros.'''

doble = [numero * 2 for numero in numeros]
print(doble)


'''En estos dos ejemplos todos los elementos de
la lista primigenia aparecen de algun modo
transformados en la nueva lista que generamos:
en el primer caso se modificaba la primera letra
de la cadena para que fuese mayuscula: En este
segundo, se multiplica el numero por dos. Ahora
bien, si queremos indicar que los elementos deben
incluirse en la nueva lista en funcion de una
condicion, podemos agregar un condicional. Por
ejemplo, el siguiente codifo crea una lista con
numeros del 1 al 100 que sean multiplos de 5.'''

multiplos5 = [numero for numero in range(1,101) if numero % 5 == 0]
print(multiplos5)

'''En funcion de estos tres ejemplos de comprension de listas
vamos a generalizar su sintaxis de la siguiente manera:

[expresion for variable in coleccion if condicion]

A traves de la comprension de listas tambien podemos expresar
de forma compacta un conjunto de bucles aninados. Por ejemplo,
el siguiente codigo crra una lista points que contiene (en forma
de tupla de dos elementos) la posicion de todos los puntos
bidimensionales entre coordenadas (0,0) y (5,10)'''

points = []

for x in range(0,5+1):
    for y in range(0,10+1):
        points.append((x,y))

print(points)

'''Ahora con la compresion de listas'''

points1 = [(x,y) for x in range(0,5+1) for y in range(0,10+1)]
print(points1)

'''Ahora imprimiremos los pares iguales'''

points2 = [(x,y) for x in range(0,5+1) for y in range(0,10+1) if x == y]
print(points2)


'''Otras colecciones

Esto que acabaos de decir se aplica por extension a otras
colecciones. Por ejemplo, podemos crear un diccionario de la
misma forma, pero en este caso utilizamos llaves en lugar de
corchetes.'''

diccionario = {n : n * 2 for n in range(1,11)}
print(diccionario)
        
