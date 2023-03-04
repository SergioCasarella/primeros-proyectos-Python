import random

def piedra_papel_tijeras():
    print("===========================")
    print("===bienvenidos al juego====")
    print("===========================")
    print("==piedra, papel o tijeras==")
    print("===========================")
    print()
    
    intentos = 3
    compu_win = 0
    humano_win = 0

    print("digita la opcion con la que quieras empezar:")
    print("1. Piedra\n2. Papel\n3. Tijeras\n")

    while intentos != 0:
        opcion_h = input("tu empizas. Elige: ").lower()
        print("has elegido: ", opcion_h,"\n")
        
        opcion_c = random.choice(["piedra","papel","tijeras"])
        print("la compu ha elegido: ",opcion_c,"\n")

        if opcion_h == opcion_c:
            print("empate!\n")
            intentos -= 1
        elif ((opcion_h == "piedra" and opcion_c == "tijera") or (opcion_h == "tijera" and opcion_c == "papel") or (opcion_h == "papel" and opcion_c == "piedra")):
            print("felicidades: Ganaste!")
            intentos -= 1
            humano_win += 1
            print("intentos restantes: ",intentos,"\n")
        else:
            print("perdiste")
            intentos -= 1
            compu_win += 1
            print("intentos restantes: ",intentos,"\n")
    
    
    print("la compu ha ganado: ",compu_win,"veces")
    print("tu has ganado: ",humano_win,"veces")

    if humano_win > compu_win:
        print("Felicidades. Has ganado el juego")
    elif humano_win == compu_win:
        print("el juego ha terminado empatado")
    else:
        print("Mala suerte. Has perdido el juego")


piedra_papel_tijeras()