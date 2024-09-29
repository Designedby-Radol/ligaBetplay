import src.modulos.clear as cle

def exitOpcion():
    global isAllow
    valid = True
    opciones = ('','N','n','S','s')
    accion = input('desea ir una pestaña atras? s(no) y enter(shi)')
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        exitOpcion()
    elif (bool(accion)== False):
        valid = False
    elif  (bool(accion) == True):
        valid = True
    return valid

def hacerMas():
    global isAllow
    valid = False
    opciones = ('','N','n','S','s')
    accion = input('desea crear otro? S(si) enter(no)')
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        cle.clearScreen()
        exitOpcion()
    elif (bool(accion)== True):
        valid = True
    elif  (bool(accion) == False):
        valid = False
    cle.clearScreen()
    return valid
