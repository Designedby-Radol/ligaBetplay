import src.modulos.see as see
import src.modulos.add as add
import src.modulos.exitProgram as ex
import src.modulos.see as see
import src.modulos.clear as cle
import os

def registroPlantel(equipos):
    papas = True
    while papas : 
        print("""
                    1. Ingresar plantel 
                    2. ingresar tecnicos
                    3. ver jugadores
                    4. salir
            """)
        decision = input('Elija la opcion a la que desea acceder: ')
        cle.clearScreen()
        match decision :
            case '1' :
                add.addPlantel(equipos)
                cle.clearScreen()
            case '2' :
                add.addTecnico(equipos)
                cle.clearScreen()
            case '3':
                see.mirarJugadores(equipos)
                cle.clearScreen()
            case '4' :
                papas = ex.exitOpcion()
                cle.clearScreen()