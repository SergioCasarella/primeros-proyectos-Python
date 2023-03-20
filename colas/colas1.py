'''
Colas

Todos sabemos lo que es una cola.

El TAD cola modela precisamente ese comportamiento: el primero que llega es el primero en ser atendido, los demas se van encolando hasta
que les toque su turno.

Sus operaciones son:

* __init__: inicializar una cola vacia.

* encolar: agrega un nuevo elemento al final de la cola.

* desencolar: elimina el primero de la cola y lo devuelve.

* es_vacia: devuelve True o False segun si la cola esta vacia o no.

Colas implementadas sobre listas

Al momento de realizar una implementacion de una cola, deberemos preguntarnos ¿Como representaremos a las colas? Veamos, en primer lugar,
si podemos implementar colas usando listas, como hicimos con la pila.

Definiremos una clase Cola con un atributo items, de tipo lista, que contendra los elementos de la cola. El primero de la cola se
encontrara en la primera posicion de la lista, y cada vez que encole un nuevo elemento, se lo agregara al final.

El metodo __init__ no recibira parametros adicionales, ya que debera crear una cola vacia (que representaremos con una lista vacia):
'''

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self,dato):
        self.items.append(dato)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError('La cola esta vacia')

    def ver_cola(self):
        print(self.items)

c1 = Cola()
c1.encolar(1)
c1.encolar(2)
c1.encolar(3)
c1.encolar(4)
c1.encolar(5)

c1.ver_cola()

c1.desencolar()
c1.desencolar()

c1.ver_cola()
