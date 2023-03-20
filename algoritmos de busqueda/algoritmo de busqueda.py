'''
El problema de la busqueda

Presentamos ahora uno de los problemas mas clasicos de la computacion, el problema de la busqueda, que se puede enunciar de la
siguiente manera:

Problema: Dada una lista xs y un valor x devolver el indice de x en xs si x esta en xs, y -1 si x no esta en xs

Estre problema tiene una solucion muy sencilla: se puede usar directamente la poderosa funcion index() de la lista.'''

milista = [3,5,7,21,98,34,65,23,0]

'''print(lista.index(5))

print(lista.index(2))'''

'''Vemos que la fncion index() resuelve nuestro problema si el valos buscado esta en la lista, pero si el valor no esta no solo
no devuelve un -1, sino que produce un error.

El problema es que para poder aplicar la funcion index() debemos estar seguros de que el valor esta en la lista, y para averiguar
eso python nos probee del operador in.'''

def comprobar(lista,n):
    if n in lista:
        posicion = lista.index(n)
        print(posicion)
    else:
        print('hola')

print(milista)
comprobar(milista, 21)

'''¿Cuantas comparaciones hace este prograa?

La pregutna del titulo se refiere a ¿Cuanto esfuerzo computacional requiere este programa' ¿Cuantas veces compara el valor que
buscamos con los datos de la lista? No lo sabemos porque no sabemos como estan implementadas ls funciones in e index().

No interesa ver que sucede si programamos la busqueda usando operaciones mas elementles, y no las grandes y primitivas in e
index(). Esto noos permitira estudiar una solucion que puede portarse a otros lenguajes que no tienen instrucciones tan poderosas.

Supongamos entonces que nuestra version de python no existe ni in ni index(). Podemos en cambio acceder a cada uno de los elementos
de la lista a traves de una construccion for, y tambien, por supuesto, podemos acceder a un elemento de la lista mediante un indice.
'''

def busqueda2(lista, x):
    i = 0

    for z in lista:
        if z == x:
            print('posicion',i)
        else:
            print('no')
            i += 1

busqueda2(milista, 5)


        

busqueda2(milista, 5)

'''¿Cuantas comparaciones hace este programa?

En el caso de encontrarlo se devuelve la posicion.

Si el valor no esta en la lista se recorre uno a uno los elementos 




