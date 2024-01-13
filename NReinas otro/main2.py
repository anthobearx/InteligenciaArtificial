from nutree import Tree, Node

arbolAncho = Tree("Busqueda a lo ancho")
l1 = arbolAncho.add(1)  # base
l2 = l1.add(2)
l3 = l2.add(5)
l4 = l3.add(9)
l4 = l3.add(10)
l3 = l2.add(6)
l4 = l3.add(11)
l4 = l3.add(12)
l5 = l4.add(17)

l2 = l1.add(3)
l3 = l2.add(7)
l4 = l3.add(13)
l4 = l3.add(14)
l5 = l4.add(18)
l3 = l2.add(8)
l4 = l3.add(15)
l4 = l3.add(16)

arbolAncho.print()

EI = arbolAncho.find(1)  #estado inicial
EO = arbolAncho.find(17)  #estado objetivo
F = [EI]  #se asigna valor inicial, frontera


def BFS(F: list[Node]):  # funcion para buscar
    if not F:
        print("Problema sin solucion, programa terminado")
        return
    else:
        EA: Node = F.pop(0)
        if goalTest(EA):
            print(f"Termino, objetivo encontrado: {EA.data}") #data para que solo imprima el 17
            return
        else:
            OS = EA.children #(funcion expand, añade los descendientes)
            for nodo in OS:
                F.append(nodo) #añade a la lista
            print(f"EA: {EA.data} \t F: {listar_Nodos(F)}")
            BFS(F) # vuelve a llamar


def goalTest(EA):
    return EA == EO  # compara si estado actual es igual a estado objetivo


def listar_Nodos(queue):
    return " ".join(str(node.data) for node in queue)

# Función para imprimir el árbol
def printTree(node, level=0):
    print("  " * level + str(node.data))
    for child in node.children:
        printTree(child, level + 1)


BFS(F)  #se llama a la funcion

