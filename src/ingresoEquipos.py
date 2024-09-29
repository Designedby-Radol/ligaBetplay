import src.modulos.add as add
import src.modulos.exitProgram as ex
import src.modulos.delete as  del_
import src.modulos.see as see
import src.modulos.clear as cle
import os 

def ingreso(equipos):
    papas = True
    while papas : 
        print("""
                    1. Ingresar equipo
                    2. Eliminar equipo
                    3. Ver equipos
                    4. Salir
            """)
        decision = input('Elija la opcion a la que desea acceder: ')
        cle.clearScreen()
        match decision :
            case '1' :
                equipos = add.addEquipos(equipos)
                cle.clearScreen()
            case '2' :
                eliminar = del_.eliminarEquipos(equipos)
            case '3' :
                mirar = see.mirarEquipos(equipos)
            case '4' :
                papas = ex.exitOpcion()
                cle.clearScreen()