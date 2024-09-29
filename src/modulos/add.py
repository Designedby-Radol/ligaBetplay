import src.modulos.see as see
import src.modulos.exitProgram as ex
import src.modulos.clear as cle
import src.modulos.fechaVal as fech

def addEquipos(equipos):
    nombre = input('Ingrese el nombre del equipo: ').strip()
    if not nombre:
        print("El nombre del equipo no puede estar vacío.")

    elif any(nombre == equipo['nombre'] for equipo in equipos):
        print(f"El equipo '{nombre}' ya existe.")
    else:
        equipos.append({'nombre':nombre,'jugadores': [],'plantel':[]})
        print(f"Equipo '{nombre}' añadido exitosamente.")
    mas = input('desea apuntar otro equipo? N(no) ingrese(si):')
    if  (bool(mas) == False) :
        addEquipos(equipos)
    else:
        print('chao')
    return equipos

def addPlantel(equipos):
    pan = True 
    while pan :
        mirar = see.elegirEquipos(equipos)
        largo = len(equipos)
        if mirar > largo or bool(mirar) == False:
            input('no puede agregar a un equipo que no existe')
            cle.clearScreen()
            return equipos
        else:
            cle.clearScreen()
            nombreJugador= input('ingrese el nombre del jugador: ')
            cle.clearScreen()
            jugadorNumero = input('ingrese numero del jugador: ')
            cle.clearScreen()
            jugadorPosicion = input('ingrese la posicion del jugador: ')
            cle.clearScreen()
            goles = input('ingrese el numero de goles del jugador: ')
            cle.clearScreen()

            while True:
                rojas = input('ingrese las tarjetas rojas del jugador: ')
                amarillas = input('ingrese las tarjetas amarillas del jugador: ')
                if rojas.isnumeric() and amarillas.isnumeric():
                    rojas = int(rojas)
                    amarillas = int(amarillas)
                    faltas = rojas + amarillas
                    break
            
            jugador = {'nombre': nombreJugador,'posicion': jugadorPosicion,'numero': jugadorNumero,'goles':goles,'faltas':faltas,'rojas':rojas,'amarillas':amarillas}
            equipos[mirar-1]['jugadores'].append(jugador)
            pan = ex.hacerMas()

def addTecnico(equipos):
    pan = True 
    while pan :
        mirar = see.elegirEquipos(equipos)
        largo = len(equipos)
        if mirar > largo or bool(mirar) == False:
            input('no puede agregar a un equipo que no existe')
            cle.clearScreen()
            return equipos
        else:
            nombre= input('ingrese el nombre del miembro: ')
            cle.clearScreen()
            labor = input('ingrese labor del miembro: ')
            cle.clearScreen()
            jugador = {'nombre': nombre,'labor':labor}
            equipos[mirar-1]['plantel'].append(jugador)
            pan = ex.hacerMas()

def addFecha(equipos,fechas):
    pan = True
    while pan:
        print("""
            ELIJA EL EQUIPO 1
        """)
        equipo1 = see.elegirEquipos(equipos)
        equipo1 -= 1
        cle.clearScreen()
        print("""
            ELIJA EL EQUIPO 2
        """)
        equipo2 = see.elegirEquipos(equipos)
        equipo2 -= 1
        cle.clearScreen()
        if equipo1 < 0 or equipo1 >= len(equipos) or equipo2 < 0 or equipo2 >= len(equipos):
            input("Error: Equipo no encontrado")
            cle.clearScreen()
            return
        dia = int(input('Ingrese el día: '))
        mes = int(input('Ingrese el mes: '))
        año = int(input('Ingrese el año: '))
        fecha = (dia, mes, año)
        fech.fecha(dia,mes, año)
        resultado = input("Ingrese el resultado del partido (Goles equipo 1 - Goles equipo 2): ")
        print(f"Partido agregado: {equipos[equipo1][0]} vs {equipos[equipo2][0]} - Fecha: {fecha} - Resultado: {resultado}")        
        if hasattr(addFecha, "fechas"):
            fechas = addFecha.fechas
        else:
            addFecha.fechas = []
        
        fechas.append({
        "equipo1": equipos[equipo1][0],
        "equipo2": equipos[equipo2][0],
        "fecha": fecha,
        "resultado": resultado
        })
        pan = ex.hacerMas()
        addFecha.fechas = fechas









