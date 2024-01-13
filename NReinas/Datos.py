# las rutas que hay en el mapa
rutasciudades = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucarest': {'Giurgiu': 90, 'Urziceni': 85, 'Pitesti': 101, 'Fagaras': 211},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Giurgiu': {'Bucarest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucarest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118, },
    'Urziceni': {'Bucarest': 85, 'Hirsova': 98, 'Vaslui': 142, },
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75},
}
#las tablas de distancia en linea recta de las ciudades
tabla_distancia_lineal = {
    'Arad': 366,
    'Bucarest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


#inicia la clase de ciudades romanianas
class ciudades_de_romania:
    nombre_cd: str = ""
    distancia_viajada: int = 0

    def __init__(self, nombre_cd: str, cd_anterior=None, distancia_viajada: int = 0) -> None: #inicializador(creacion de objetos)
        self.nombre_cd = nombre_cd
        self.cd_anterior = cd_anterior
        self.distancia_viajada = distancia_viajada

    def goal_test(self) -> bool:  # ciudad meta
        return self.nombre_cd == "Bucarest"

    def expand(self) -> list:  # se calcula distancia, y se obtienen los nodos que colindan
        for descendiente in rutasciudades[self.nombre_cd]:  # se obtienen sus respectivos descendientes
            nueva_distancia: int = self.distancia_viajada + rutasciudades[self.nombre_cd][
                descendiente]  # se calcula su nuevo valor
            descendiente.append(ciudades_de_romania(nombre_cd=descendiente, cd_anterior=self,
                                                   distancia_viajada=nueva_distancia))  # aqui va el descendiente del nodo
        return descendiente

    def distancia_heuristica(self) -> int:  #calcular h (se obtiene)
        return self.distancia_viajada + tabla_distancia_lineal[self.nombre_cd]

    def __repr__(self) -> str: #metodo tostring pero en python
        return f"Ciudad: {self.nombre_cd:10}, Distancia recorrida: {str(self.distancia_viajada):>5}, Heuristica: {str(self.distancia_heuristica()):>5}{f', Ciudad anterior: {self.cd_anterior.nombre_cd}' if self.cd_anterior != None else ''}"

#metodo que imprime la ruta seguida
def ruta_tostring(ultima_cd: ciudades_de_romania,
                  ruta: str = "") -> str:  # Función que recibe una ciudad y retorna un string con la ruta que se tomó para llegar a ella
    ruta = (ultima_cd.nombre_cd + "(" + str(ultima_cd.distancia_viajada) + ") -> ") + ruta
    if ultima_cd.cd_anterior != None:
        return ruta_tostring(ultima_cd.cd_anterior, ruta)
    else:
        return ruta[0:-4]

#obtiene la ruta
def lista_ruta(ultima_cd: ciudades_de_romania, route: list[str] = []) -> list[
    str]:
    route.append(ultima_cd.nombre_cd)
    if ultima_cd.cd_anterior != None:
        return lista_ruta(ultima_cd.cd_anterior, route)
    else:
        return route


def a_estrella(frontera: list[ciudades_de_romania]) -> str: #besuqueda de a estrella
    if frontera == []:  # si esta vacio, termina
        return "Solucion no encontrada", None
    ciudad_actual = frontera.pop(0)  # se hace pop a f (se quita primer elemento y se añade a f)
    print(ciudad_actual)
    if ciudad_actual.goal_test():  # se vertifica si se llego a la cd de bucarest
        return "Solucion encontrada", ciudad_actual
    descendientess = ciudad_actual.expand()  # obtenemos las ciudades que colindan de la cd actual
    frontera += descendientess  # se añaden descendientes a la frontera
    frontera.sort(key=ciudades_de_romania.distancia_heuristica)  # se ordena de menor a mayor de acuerdo al cualculo de h

    return a_estrella(frontera)