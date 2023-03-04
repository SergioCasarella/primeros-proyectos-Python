# Informacion de la biografia

def biografia():
    nom = input('Ingrese su nombre: ')
    if nom == '' or nom == '*':
        print('entrada incorrecta')
    fecha = input('Ingrese su fecha de nacimiento: ')
    if fecha == '' or fecha == '*':
        print('entrada incorrecta')
    print(nom,fecha)

biografia()
