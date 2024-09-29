import src.ingresoEquipos as ing
import src.registroPlantel as reg
import src.modulos.exitProgram as ex
import src.modulos.see as see
import src.modulos.clear as cle
import src.modulos.add as add

equipos = []
fechas = []
def menu ():
    try:
        mondongo = True
        global equipos,fecha
        while mondongo == True:
            print("""
                        1. Ingresar equipos de torneos
                        2. Ingresar jugadores de equipos
                        3. programar partidos(fecha)
                        4. Ver resultados de partidos
                        5. salir
                """)
            decision = input('Elija la opcion a la que desea acceder: ')
            cle.clearScreen()
            match decision :
                case '1' :
                    ing.ingreso(equipos)
                case '2' :
                    reg.registroPlantel(equipos)
                case '3' :
                    add.addFecha(equipos,fechas)
                case '4' :
                    see.verResultados()
                case '5':
                    mondongo = ex.exitOpcion()
                    cle.clearScreen()
    except ValueError:
        input('Ingreso invalido, intente nuevamente.')
        cle.clearScreen()
        menu()

