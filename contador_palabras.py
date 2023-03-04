# Contador de palabras

def contador_Palabras():
    frase = input("¿En qué estas pensando?")
    numpalabras = 0

    frase1 = frase.split()

    for palabra in frase1:
        numpalabras += 1
    print('el texto contiene',numpalabras,'palabras')

contador_Palabras()
