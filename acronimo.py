# Acronimo

def acronimo():
    bandera = "s"
    while bandera == 's':
        acro = input('ingrese organizacion o concepto: ')
        lista = acro.split(' ')
        print('Acronimo de:',acro)
        for palabra in lista:
            print(palabra[0],end='')
        break

    bandera = input('\ndesea continuar? s/n: ')


acronimo()
