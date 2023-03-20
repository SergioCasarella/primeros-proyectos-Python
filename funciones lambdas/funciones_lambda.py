saludar = lambda nombre: print(f"hola {nombre}!!")

saludar("Pablo")
saludar("Juan")

# LLamar funciones dentro una lambda

maximo = lambda a,b,c: f"El maximo entre {a},{b},{c} es {max(a,b,c)}"
print(maximo(5,7,1))
print(maximo(4,87,109))

# Funciones lambda dentro de funciones
# Podemos definir funciones lambdas dentro de funciones convencionales

def ponerPrefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"

addMr = ponerPrefijo("Mr")

print(addMr("Pablo"))

def elevarA(exponente):
    return lambda numero: f"{numero ** exponente}"

cuadrado = elevarA(2)
cubo = elevarA(3)

print(cuadrado(3))
print(cubo(3))
print(cuadrado(4))
print(cubo(4))