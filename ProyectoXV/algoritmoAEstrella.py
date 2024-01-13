from ciudadesEuropeas import rutas_grafo, distancias_lineales
#capitales = [
#    "Amsterdam", "Berlin", "Bruselas", "Budapest", "Copenhague", "Madrid", "Paris", "Praga", "Roma", "Varsovia",
#    "Viena", "Zurich"  # Aunque Zúrich no es la capital, es una ciudad principal
#]
ciudad_destino = "Zurich"


#def obtenerNuevaMeta(listaCiudades: list):
#    if len(listaCiudades['values']) > 0:
#        ciudad_destino = listaCiudades.pop(0)#qutar el primero de la lista, y añadirlo a ciudad_destino
#        return ciudad_destino

class claseciudad: #inicio de la clase ciudad, se usa para la creacion de objetos ciudad y usar sus atributos
    nombre_ciudad: str = ""
    distancia_trasladada: int = 0

    def __init__(self, nombre_ciudad: str, ciudad_anterior=None, distancia_trasladada: int = 0) -> None:
        self.nombre_ciudad = nombre_ciudad
        self.ciudad_anterior = ciudad_anterior
        self.distancia_trasladada = distancia_trasladada

    def goal_test(self) -> bool:  # goaltest
        return self.nombre_ciudad == ciudad_destino

    def expand(self) -> list:  # Expand, obtienen los offsprings o descendientes (colindantes de la ciudad)
        off_springs: list[claseciudad] = []
        for off_spring in rutas_grafo[self.nombre_ciudad]:  # Un for que saca los descendientes de cada ciudad
            distancia: int = self.distancia_trasladada + rutas_grafo[self.nombre_ciudad][off_spring]  # Se saca distancia a las ciudades descendientes
            off_springs.append(claseciudad(nombre_ciudad=off_spring, ciudad_anterior=self, distancia_trasladada=distancia))
            # Se añaden offsprings
        return off_springs

    def heuristica(self) -> int:  # Sacar heuristica de una ciudad
        return self.distancia_trasladada + distancias_lineales[ciudad_destino][self.nombre_ciudad]
        #f(x)=        #g(x)              +         h(x)


    def __repr__(self) -> str:
        return f"Ciudad: {self.nombre_ciudad:15} Distancia trasladada: {str(self.distancia_trasladada):10} Heuristica: {str(self.heuristica()):>5}"


def rutasAEstrella(ultima_ciudad: claseciudad, ruta: str = "") -> str:  # Función que recibe una ciudad y retorna un string con la ruta que se tomó para llegar a ella
    ruta = ("\'" + ultima_ciudad.nombre_ciudad + "', ") + ruta
    if ultima_ciudad.ciudad_anterior != None:
        return f"{str(ultima_ciudad.distancia_trasladada):>4}" + ", " + rutasAEstrella(ultima_ciudad.ciudad_anterior, ruta)
    else:
        return ruta[0:-2]


def lista_de_rutas(ultima_ciudad: claseciudad, rutas: list[str] = []) -> list[str]: # La lista de ciudades
    rutas.append(ultima_ciudad.nombre_ciudad)
    if ultima_ciudad.ciudad_anterior != None:
        return lista_de_rutas(ultima_ciudad.ciudad_anterior, rutas)
    else:
        return rutas


def aestrella(frontier: list[claseciudad]) -> tuple[str, claseciudad]:  # Busqueda a estrella
    if frontier == []:  # Se comprueba si frontera esta vacio
        return "Solucion no encontrada", None
    nombre_ciudad = frontier.pop(0)  # Popeamos primer elemento de frontera y guardamos en la variable
    print(nombre_ciudad) #usa el metodo rerpr (tostring en python)
    if nombre_ciudad.goal_test():  # Se comprueba si se llego a la meta
        return "Solucion encontrada", nombre_ciudad
    off_springs = nombre_ciudad.expand()  # Se obtienen descendientes (colindantes) de ciudad actual
    frontier += off_springs  # Se agregan los descendientes a frontera
    frontier.sort(key=claseciudad.heuristica)  # Se acomoda por heuristica

    return aestrella(frontier)
