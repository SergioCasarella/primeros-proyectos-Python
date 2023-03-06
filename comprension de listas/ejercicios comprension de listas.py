#Ejercicios

'''
1) Crear una lista con las iniciales de las palabras de la
lista dada:
'''

palabras = ['casa','mesa','silla','puerta','ventana']

iniciales = [palabra[0] for palabra in palabras]
print(iniciales)

'''
2) Crear una lista que contenga solo los numeros pares
tomando en cuenta la siguiente lista:
'''

datos = [14,18,21,29,36,41,58,63,74]

pares = [x for x in datos if x % 2 == 0]
print(pares)

'''
3) Crear una lista con las palabras de la lista dada
que tengan mas de 7 letras
'''

utensilios = ['mesa','interruptor','silla','microfono','cubo']

mas7letras = [palabra for palabra in utensilios if len(palabra) > 7]
print(mas7letras)

'''
4) Crear una lista con el numero siguiente la los numeros
del 1 al 30 que sean multiplos de 7 o multiplos de 11
'''

mult7 = [x + 1 for x in range(1,31) if x % 7 == 0 or x % 11 == 0]
print(mult7)

'''
5) Crear una lista que imprimma los numeros pares
pero los impares los asigne con un 0.
'''

datos1 = [2,3,5,8,9,10,12,15]
impar0 = [x if x % 2 == 0 else 0 for x in datos]
print(impar0)

'''
6) Crear una lista con el tipo de datos de cada uno de los
elementos que incluye la lista datos2:
* Si son cadenas de caracter: 'cadena'
* Si son enteros o float: 'numerico'
'''

datos2 = [7,'h',2.5,'m',8.2,24,'p']

tipos = ['cadena' if type(dato) == str else 'numerico' for dato in datos2] 
print(tipos)

datos3 = [7,'h',2.5,'m',8.2,24,'p']

tipos2 = ['cadena' if isinstance(dato, str) else
          'entero' if isinstance(dato, int) else
          'float' for dato in datos3]

print(tipos2)
