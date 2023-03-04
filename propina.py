# Propina

def propina():
    bandera = 's'
    while bandera == 's':
        print('Bienvenido a tu calculador de propinas!')
        total = float(input('¿Cual es el total de hoy, por favor? '))
        carga = 18
        propina = (total * carga) / 100
        totalConPropina = total + propina
        salida = input('La propina aplicando el '+str(carga)+' % es:'+str(propina)+'. Lo que hace un total de: '+str(totalConPropina)+' pesos')
        bandera = input('Desea continuar? s/n: ')

propina()
                    
