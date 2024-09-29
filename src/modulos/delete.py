import src.modulos.see as see
import src.modulos.clear as cle
import os

def eliminarEquipos(equipos):
    mirar =int(see.eliminarEquipos(equipos))
    largo = len(equipos)
    if mirar > largo or bool(mirar) == False:
        input('no puede eliminar equipos que no existen')
        cle.clearScreen()
        return equipos
    else:
        cle.clearScreen()
        equipos.pop(mirar-1)
    cle.clearScreen()

