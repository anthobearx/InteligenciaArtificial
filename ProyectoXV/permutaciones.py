from itertools import permutations
from ciudadesEuropeas import rutas_posibles_ciudades


# sacar todas las permutaciones de todos x todos
def permutaciones(ciudadInicial: str, listaporvisitar: list[str]) -> list[
    list[str]]:
    listaPermutaciones: list[list[str]] = []
    for permutation in list(permutations(listaporvisitar)):
        listaPermutaciones.append([ciudadInicial] + list(permutation) + [ciudadInicial])
    return listaPermutaciones

def imprimirPermutaciones(ciudadInicial, lista):
    lista_rutas = permutaciones(ciudadInicial, lista)
    for ruta in lista_rutas:
        print(rutasPermutadasToString(ruta))




# Evalua las rutas
def evaluate_permutacion(lista_ciudades: list[str]) -> int:
    kmRecorridos = 0
    for ciudad in lista_ciudades:
        siguiente_ciudad = lista_ciudades[lista_ciudades.index(ciudad) + 1]#obtener la primera ciudad
        for ruta in rutas_posibles_ciudades:
            #busca en la lista rutas_posibles_ciudades para comparlas, y ver cual es la sig
            if (ruta[1] == ciudad and ruta[-1] == siguiente_ciudad) or (ruta[-1] == ciudad and ruta[1] == siguiente_ciudad):
                kmRecorridos += ruta[0]
                break
    return kmRecorridos


def rutaOptima(ciudadOrigen: str, listaCiudades: list[str]) -> (list[str], int):#regresa la ruta que tiene menos viaje
    permutaciones_temp = permutaciones(ciudadOrigen, listaCiudades)
    permutaciones_temp.sort(key=evaluate_permutacion)
    return permutaciones_temp[0], evaluate_permutacion(permutaciones_temp[0])


def rutasPermutadasToString(listaciudades: list[str]) -> str:
    return " --> ".join(listaciudades).upper()
