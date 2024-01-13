blacklist = []

class tablero():
    nivel = 0 #se utiliza en el limitado, demuestra el maximo nivel de busqueda
    reinas = []#posiciones de las reinas(EA)
    visitado = []#posiciones ya visitadas, saltarlas(lista negra)
#init es el constructor
    def __init__(self, visitado: list, nivel: int = 0, tamano: int = 4, reinas: list[int] = [], ) -> None:
        self.visitado = visitado
        self.nivel = nivel
        self.tamano = tamano
        if reinas == []:#si reinas esta vacio
            self.reinas = [0] * tamano#los hace todos a 0
        else:#si no (entra con los descendientes de los tablero)
            self.reinas = reinas#usa los valores que tu asignas
        if self.reinas not in visitado: self.visitado.append(self.reinas)#agrega estado al visitado (blacklist) si no esta

    def ataques(self) -> int:  #funcion ataque, que recibe el objeto tablero y regresa los ataques encontrados
        n = len(self.reinas)
        A = 0 # numero de ataques
        for i in range(n):
            for j in range(i + 1, n):
                if self.reinas[i] == self.reinas[j]: #deteminamos cantidad de atacaques en  H y V 
                    A += 2
                if abs(i - j) == abs(self.reinas[i] - self.reinas[j]):#deteminamos cantidad de atacaques en diagonal
                    A += 2
        return A

    def goal_test(self) -> bool:  # funcion que regresa true si los ataques son 0
        return self.ataques() == 0

    def expand(self) -> list:  #obtener la descendencia (primeros metodos de 4 reinas)
        expancion = []
        aux = []
        for i in range(self.tamano):#recorre las reinas
            aux += self.reinas#copia el estado, trabajar sobre una copia
            if aux[i] + 1 < self.tamano: #checa si el estado que sigue no sobrepasa el limite del tablero
                aux[i] += 1#aumenta 1 en aux, para agregar el nuevo nodo
            if aux not in self.visitado:#si no esta en visitados, se salta, si esta, lo agrega
                expancion.append(tablero(visitado=self.visitado, nivel=self.nivel + 1, tamano=self.tamano, reinas=aux))
            aux = []
        return expancion


    def reset_visited(self) -> None:  # Función para reinicial la lista de estados visitados (iterado)
        self.visitado.clear

    def __repr__(self) -> str: #devuelve valor estado (metodo similar a tostring en java)
        return "estado: " + str(self.reinas)


def bf_s(frontier: list[tablero]) -> tuple[str, tablero]:  # Función de búsqueda Breadth-First Search (ancho)
    if frontier == []: #si la Frontera es nula no existe solucion
        return "Solucion no encontrada o inexistente", None
    current_state: tablero = frontier.pop(0) #el valor de frontera  se añade al estado actual
    print(current_state) #se imprime el estado actual
    if current_state.goal_test():#si en el estado actual es 0 imprime la solucion
        return "Solucion encontrada: " + str(current_state), current_state
    off_springs = current_state.expand() #se añaden los nuevos nodos del estado actual
    frontier = frontier + off_springs # añade los nuevos nodos al final en frontera

    return bf_s(frontier)


def df_s(frontier: list[tablero]) -> tuple[str, tablero]:  # Función de búsqueda Depth-First Search (profundo)
    if frontier == []:#si la Frontera es nula no existe solucion
        return "Solucion no encontrada o inexistente", None
    current_state: tablero = frontier.pop(0) #el valor de frontera  se añade al estado actual
    print(current_state)#se imprime el estado actual
    if current_state.goal_test():#si en el estado actual es 0 imprime la solucion
        return "Solucion encontrada: " + str(current_state), current_state
    off_springs = current_state.expand() #se añaden los nuevos nodos del estado actual
    frontier = off_springs + frontier # añade los nuevos nodos al inicio en frontera

    return df_s(frontier)


def dl_s(frontier: list[tablero], limit: int) -> tuple[str, tablero]:  # Función de búsqueda  (Limitado)  Depth-Limited Search
    if frontier == []: #si la Frontera es nula no existe solucion
        return "Solucion no encontrada o inexistente", None
    current_state: tablero = frontier.pop(0)  #el valor de frontera  se añade al estado actual
    current_level = current_state.nivel # el valor de nivel  se añade al estado actual
    print(current_state)#se imprime el estado actual
    if current_state.goal_test(): #si en el estado actual es 0 imprime la solucion
        return "Solucion encontrada: " + str(current_state), current_state
    if current_level >= limit: #si en el nivel mayor o igual al limite   se imprime el mensaje de aviso
        return "Limite alcanzado", None
    off_springs = current_state.expand() #se añaden los nuevos nodos del estado actual
    frontier = off_springs + frontier  # añade los nuevos nodos al inicio en frontera

    return dl_s(frontier, limit)

                                                                #iterado
def idl_s(game: tablero, limit: int, increment: int) -> tuple[
    str, tablero]:  # Función de búsqueda Iterated Depth-Limited Search (cuando llega al limite, lo aumenta, y reintenta)
    while True:
        frontier = []
        frontier.append(game) # se añaden a frontera el estado actual
        game.visitado = [] #lista vacia
        message, goal = dl_s(frontier, limit) #mensaje y meta del metodo
        if goal != None: #si meta es diferente a ninguna, pues ya hay meta
            return message + ", limite: " + str(limit), goal
        print(message)
        limit += increment#aumentar el limite con el incremento



def g_s(frontier: list[tablero]):
    g_s.counter += 1 #contador de veces que se ejecuta el voraz
    print("i: ", g_s.counter)
    print(frontier, "\n")
    if frontier == []:
        return "Solucion no encontrada o no existente", None
    else:
        current_state = frontier

        if tablero.goal_test(current_state):
            print("> Se encontró la solución para ", tablero.reinas, " reinas: ")
            print(current_state)
            #print_tablero(current_state)
            return current_state
        else:
            offsprings = expandVoraz(current_state)
            order = evaluateVoraz(offsprings)
            offsprings = ord_burbuja(offsprings, order) #ordena por metodo de burbaja
        if offsprings: #si no esta vacio
            g_s(offsprings[0])#vuelve a llamar con el primer descendiente
        else:
            g_s([])#lo llama sin nada


g_s.counter = 0

def expandVoraz(vector):#obtiene los descendientes del nodo
    copy = vector.copy()
    offspring_states = []
    blacklist.append(vector)

    for fila in range(0, vector.count()):
        for columna in range(0, vector.count()):
            # Mueve la reina en la columna actual
            new_value = (vector[columna] + fila) % vector.count()
            vector[columna] = new_value
            if vector not in blacklist:
                offspring_states.append(vector)#agregamos el nuevo decendiente

            vector = copy.copy()

    return offspring_states

def evaluateVoraz(offsprings):#unicamente obtiene los ataques de cada nodo
    number_attacks = []#crea una lista
    for child in offsprings:
        number_attacks.append(child.ataques) #los ataques de cada hijo

    return number_attacks


def ord_burbuja(offsprings, orden): #metodo de ordenamiento de la burbuja
    intercambio = False

    for n in range(len(orden) - 1, 0, -1):
        for i in range(n):
            if orden[i] > orden[i + 1]:
                intercambio = True
                orden[i], orden[i + 1] = orden[i + 1], orden[i]
                offsprings[i], offsprings[i + 1] = offsprings[i + 1], offsprings[i]
        if not intercambio:
            break

    return offsprings
