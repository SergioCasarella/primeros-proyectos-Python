# palindromo

def palindromo():
    bandera = 's'
    while bandera == 's':
        pal = input('ingrese una palabra: ')
        rev = pal[::-1]
        if pal == rev:
            print('es una palabra palindroma')
        else:
            print('no es una palabra palindroma')
        bandera = input('desea continuar? s/n: ')

palindromo()
