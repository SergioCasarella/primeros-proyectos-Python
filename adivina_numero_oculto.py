# Adivina el numero oculto

numero = 35

def numOculto():
    print('Intenta adivinar un numero oculto que esta entre 0 y 50')
    bandera = 's'
    while bandera == 's':
        pregunta = int(input('ingresa el numero: '))
        if pregunta > 50:
            print('Error! estas fuera de rango!')
        elif pregunta < 1:
            print('Error! estas fuera de rango!')
        elif pregunta < numero:
            print('Intenta con un numero mayor!')
        elif pregunta > numero:
            print('Intenta con un numero menor')
        else:
            print('Felicidades! Has acertado!')

        bandera = input('Deseas continuar? s/n: ')
        
            
        
numOculto()       
