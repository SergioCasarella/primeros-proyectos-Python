# Par o impar

def par_Impar():
    print('Bienvenido a Par o impar')
    bandera = 's'
    while bandera == 's':
        num = int(input("Dime el numero que quieres analizar: "))
        if num % 2 == 0:
            print(num,'es un numero par')
        else:
            print(num,'es un numero impar')
        bandera = input('¿deseas continuar? s / n: ')

par_Impar()