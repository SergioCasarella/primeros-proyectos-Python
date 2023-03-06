#comprension de listas con funciones
import math

val_decimales = [1.23453, 2.344534564, 3.84745095]

val_redondeados = [round(val, 2) for val in val_decimales]
print(val_redondeados)


minusculas = ['mesa','silla','puerta','ventana','armario']

mayusculas = [n.upper() for n in minusculas]
print(mayusculas)

minusculas1 = [nombre.lower() for nombre in mayusculas]
print(minusculas1)

'''Lista con la superficie de circulos teniendo en cuenta los siguientes radios'''

radio_circulos = [7,12,21,32,41]

area_circulos = [round((n*n) * 3.14,2) for n in radio_circulos]
print(area_circulos)

area_circulos1 = [round((math.pi * r**2),2) for r in radio_circulos]
print(area_circulos1)

def area_circulo(r):
    return math.pi * r**2

area_circulos2 = [round(area_circulo(r),2) for r in radio_circulos]
print(area_circulos2)


