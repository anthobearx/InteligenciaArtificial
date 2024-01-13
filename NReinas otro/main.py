# patron por niveles, busqueda a lo ancho

from collections import deque
import pickle


# clase para crear arboles
class TreeNode:
    # funciones para crear nodos y sus respectivos hijos
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def imprimir_arbol(root):
    if not root:
        return

    queue = deque()
    queue.append(root)

    while queue:
        nodo_actual = queue.popleft()
        print(nodo_actual.value, end=' ')

        for hijo in nodo_actual.children:
            queue.append(hijo)


# Crear los nodos del arbol
nodo1 = TreeNode(1)
nodo2 = TreeNode(2)
nodo3 = TreeNode(3)
nodo5 = TreeNode(5)
nodo6 = TreeNode(6)
nodo7 = TreeNode(7)
nodo8 = TreeNode(8)
nodo9 = TreeNode(9)
nodo10 = TreeNode(10)
nodo11 = TreeNode(11)
nodo12 = TreeNode(12)
nodo13 = TreeNode(13)
nodo14 = TreeNode(14)
nodo15 = TreeNode(15)
nodo16 = TreeNode(16)
nodo17 = TreeNode(17)
nodo18 = TreeNode(18)

# Establecer las relaciones entre los nodos
nodo1.add_child(nodo2)
nodo1.add_child(nodo3)
nodo2.add_child(nodo5)
nodo2.add_child(nodo6)
nodo3.add_child(nodo7)
nodo3.add_child(nodo8)
nodo5.add_child(nodo9)
nodo5.add_child(nodo10)
nodo6.add_child(nodo11)
nodo6.add_child(nodo12)
nodo7.add_child(nodo13)
nodo7.add_child(nodo14)
nodo8.add_child(nodo15)
nodo8.add_child(nodo16)
nodo12.add_child(nodo17)
nodo14.add_child(nodo18)

# Serializar el arbol y guardarlo en un archivo
with open('arbol_busqueda_ancho.pickle', 'wb') as archivo:
    pickle.dump(nodo1, archivo)

# cargar el arbol de nuevo desde el archivo
with open('arbol_busqueda_ancho.pickle', 'rb') as archivo:
    arbol_recuperado = pickle.load(archivo)

# Ahora, `arbol_recuperado` contiene el árbol que guardaste anteriormente


# imprimir el arbol
# imprimir_arbol(nodo1)


EI = nodo1.value  # estado inicial
EO = nodo17.value  # estado objetivo

F = [EI]  # lista con valor inicial
OS = []  # lista OS


def BFS(F: list):  # funcion para buscar
    if isEmpty(F):
        print("Problema sin solucion, programa terminado")
        return
    else:
        EA = F.pop(0)  # sacar primer valor de f, y ponerlo en estado actual
        if goalTest(EA):
            print(f"Termino, objetivo encontrado: {EA}")
            return
        else:
            OS = expand(EA)  # buscar e implementar una manera de que en OS se guarden los hijos de EA
            F.append(OS)
            print("procesando..")
            BFS(F)

def goalTest(EA):
    return EA == EO  # compara si estado actual es igual a estado objetivo


def isEmpty(F):
    return len(F) == 0


def expand(EA):
    listaHijos = []
    for nodo in arbol_recuperado.children:
        listaHijos.append(nodo.value)
    return listaHijos

BFS(F)
print(OS)
print(F)