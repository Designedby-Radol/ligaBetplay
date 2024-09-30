import src.modulos.clear as cle
import src.modulos.add as add

def mirarEquipos(equipos):
    if equipos:
        print("Equipos disponibles:")
        for i, equipo in enumerate(equipos, start=1):
            print(f"{i}: {equipo['nombre']}")
        print('')
    else:
        print('No hay equipos registrados. \n')
    input('presione enter para salir:')
    cle.clearScreen()

def mirarJugadores(equipos):
    e = 0
    for i, equipo in enumerate(equipos, start=1):
        print(f"{i}.Equipo: {equipo['nombre']}")
        print("""
                JUGADORES
            """)
        for jugador in equipo['jugadores']:
            e=+1
            print(f"  {e} Nombre del jugador: {jugador['nombre']}")
            print(f"  - Posición: {jugador['posicion']}")
            print(f"  - Número: {jugador['numero']}")
            print(f"  - faltas: {jugador['faltas']}")
            print(f"  - rojas: {jugador['rojas']}")
            print(f"  - amarillas: {jugador['amarillas']}")
        print("""
                PLANTEL
            """)
        e = 0
        for plantel in equipo['plantel']:
            e=+1
            print(f"  {e}. nombre del {plantel['labor']}: {plantel['nombre']}")
        print('')
    print('')
    print('presione para salir:')
    input('')


def eliminarEquipos(equipos):
    if equipos:
        print('Equipos actuales: \n')
        for i, equipo in enumerate(equipos, start=1):
            print(f"{i}: {equipo['nombre']}")
        print('')
        a = int(input('ingrese el numero del equipo que desea eliminar: '))
        return a 
    else:
        print('No hay equipos registrados. \n')
        return False

def elegirEquipos(equipos):
    if equipos:
        print("Equipos disponibles:")
        for i, equipo in enumerate(equipos,start=1):
            print(f"{i}: {equipo['nombre']}")
        print('')
        a = int(input('ingrese el numero del equipo que desea: '))
        return a 
    else:
        print('No hay equipos registrados. \n')
        return False

def verResultados():
    if hasattr(add.addFecha, "fechas"):
        fechas = add.addFecha.fechas
        if fechas:
            print("Fechas de partido:")
            for fecha in fechas:
                print(f"{fecha['equipo1']} vs {fecha['equipo2']} - Fecha: {fecha['fecha']} - Resultado: {fecha['resultado']}")
            input('')
            cle.clearScreen()
        else:
            print("No hay fechas de partido agregadas")
            input("")
            cle.clearScreen()
    else:
        print("No hay fechas de partido agregadas")
        input("")
        cle.clearScreen()