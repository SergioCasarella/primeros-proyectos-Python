
personas = [['jorge',36],['silvia',24],['tomas',47],['irene',19],['ignacio',21],['julia',43]]

edades = [[persona[0],'mayor'] if persona[1] > 30 else [persona[0],'menor'] for persona in personas]
print(edades)

edades1 = [[persona[0],'mayor' if persona[1] > 30 else 'menor'] for persona in personas]#la condicion if else se puede colocar dentro de los corchetes
print(edades1)

inventario = {'puntas':30,
              'tornillos':140,
              'tuercas':250,
              'arandelas':70}


#pedidos = [articulo for articulo in inventario if inventario[articulo] < 100]

pedidos = [clave for clave,valor in inventario.items() if valor < 100]
print(pedidos)

pedidos2 = [valor for clave,valor in inventario.items() if valor > 100]
print(pedidos2)

'''Crear una lista con los alumnos cuya nota sea cinco o mas'''

alumnos = [{'nombre':'claudia','nota':9,'grupo':'a'},
           {'nombre':'esteban','nota':4,'grupo':'b'},
           {'nombre':'silvia','nota':7,'grupo':'c'},
           {'nombre':'jorge','nota':3,'grupo':'b'},
           {'nombre':'roberto','nota':6,'grupo':'a'}]

aprobados = [alumno['nombre'] for alumno in alumnos if alumno['nota'] >= 5]
print(aprobados)

'''Crear una lista con los alumnos que hayan aprobado la asignatura de lengua'''

alumnos1 = {'claudia':{'matematica':8,'lengua':7,'ingles':6},
            'esteban':{'matematica':7,'lengua':3,'ingles':8},
            'silvia':{'matematica':5,'lengua':5,'ingles':9}}


aprobadosLengua = [alumno for alumno,asignaturas in alumnos1.items()
              if asignaturas['lengua'] >= 5]
print(aprobadosLengua)


aprobadosMat = [nombre for nombre,asignaturas in alumnos1.items()
                if asignaturas['matematica'] >= 5]
print(aprobadosMat)
