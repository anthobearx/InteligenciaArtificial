import sys
from tablero import ChessboardGUI


def evaluate(os):#evalua quien tiene menos ataques
    n = len(os) #obtiene la longitud del la lista (numeros de posiciones)
    #print(n)
    #evaluados = []#lista donde se guardara cuantos ataques tiene cada vector
    for i in range(n):#recorre OS
        evaluados.append(ataques(os[i])) #agrega cuantos ataques tiene cada vector en una listaratio de devoluciones a través del tiempo
    return evaluados

    #print(evaluados)
    #print(os)
    #sort(os)


def sort(os):#acomoda la lista de arreglos de menor ataque a mas ataque
    combinados = list(zip(evaluados, os)) # Combinar evaluados y OS en una lista de tuplas

    #
    combinados.sort(key=lambda x: x[0]) #Ordena la lista de tuplas en función de los valores en evaluados
    # Separa los valores ordenados de vuelta en evaluados y OS
    evaluados_ordenados, OS_ordenado = zip(*combinados)

    #print(evaluados_ordenados)  # [0, 10, 12, 12]
    #print(OS_ordenado)  # [[1, 3, 0, 2], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return OS_ordenado




def expand(ea):  # recibe el estado actual
    n = len(ea)  # obtiene la longitud de ea
    ne = []  # crea una lista
    for i in range(n):
        aux = list(ea)  # guarda ea en aux
        posicion = aux[i]  # posicion es igual al valor actual de auxiliar
        if (posicion < n - 1):  # comprueba de que posicion este dentro del rango del tablero
            posicion += 1  # aumenta 1
            aux[i] = posicion  # aux toma el valor de posicion
            if aux not in visitados:  # si aux no ha sido visitado
                ne.append(aux)  # se agrega a la lista de nodos
    return ne


#recibe un vector y compara una posicion con otra (todas con todas), y si estas coinciden de forma horizontal, vertical, o diagonal, se suman dos ataques (1 de cada reina, osea 2)
def ataques(v):
    # print("Vector ",v)
    ataques = 0
    n = len(v)
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] == v[j]:
                ataques += 2
            if abs(i - j) == abs(v[i] - v[j]):
                ataques += 2
    # print("Ataques ",ataques)
    return ataques


def goaltest(ea): #la meta es que ataques sea = 0
    return ataques(ea) == 0


def B_profunda(f, limite):
    if not f:  # si f esta vacio, no hay solucion
        print("No hay solucion")
        return False
    else:
        ea = f[0][0]  # estado actual
        na = f[0][1]  # nivel actual
        visitados.append(ea)  # agrega ea en visitados
        print("Edo_act ", ea, " Nivel", na)  # imprime el ultimo visitado
        f.pop(0)  # se quita el primer valor
        if goaltest(ea):  # comprueba si el objetivo es el indicado (0 ataques)
            print("Termine; Objetivo logrado", ea)
            gui = ChessboardGUI(4, visitados)
            return True
        elif (limite > na):
            OS = expand(ea)  # añadir siguiente movimiento
            #print("OS: ", OS)
            evaluate(OS)
            OS = sort(OS)
            # print("OS ",OS)
            for os in OS:
                f.insert(0, [os, na + 1])  # inserta en f el arreglo y aumenta uno su nivel
        return B_profunda(f, limite)


def B_iterada():
    limite = 2
    band = False  # bandera en falso
    while (band is not True):  # mientras no sea falso, se repite
        f = [[[0, 0, 0, 0],0]]  # lista frontera, en donde se guardan las posiciones de las reinas, y su nivel de profundidad
        visitados.clear()  # se borra el arreglo de visitados
        band = B_profunda(f, limite)  # bandera sera igual a lo que regrese dfs(funcion de busqueda de profundidad)
        limite += 2  # aumenta en dos el limite


sys.setrecursionlimit(1000000000)  # establecimiento de limite de recursividad, evita desbordamiento
visitados = []  # creacion de una lista vacia
evaluados = []#lista donde se guardara cuantos ataques tiene cada atomo del vector
#B_iterada()  # se llama a la funcion de busqueda iterada


#testing
os = [[0,0,0,0],[0,1,0,0],[1,3,0,2],[0,0,0,0]]
print(evaluate(os))
os = sort(os)
print(os)
