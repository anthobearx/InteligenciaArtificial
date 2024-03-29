
n = 50  # tablero (n * n)
f = [0] * n  # [0, 0, 0, 0], n = 4
blacklist = []  # configuraciones visitadas
iteraciones = 0


# Voraz
def greedys(f):
    greedys.counter += 1 #contador de veces que se ejecuta el voraz
    print("i: ", greedys.counter)
    print(f, "\n")
    if not f:
        print("> No hay solución")
        return False
    else:
        actual_state = f

        if goal_test(actual_state):
            print("> Se encontró la solución para ", n, " reinas: ")
            print(actual_state)
            print_board(actual_state)
            return True
        else:
            offsprings = expand(actual_state)
            order = evaluate(offsprings)
            offsprings = bubble_sort(offsprings, order) #ordena por metodo de burbaja
        if offsprings: #si no esta vacio
            greedys(offsprings[0])#vuelve a llamar con el primer descendiente
        else:
            greedys([])#lo llama sin nada


greedys.counter = 0


def goal_test(test):
    return attacks(test) == 0


def expand(vector):#obtiene los descendientes del nodo
    copy = vector.copy()
    offspring_states = []
    blacklist.append(vector)

    for fila in range(0, n):
        for columna in range(0, n):
            # Mueve la reina en la columna actual
            new_value = (vector[columna] + fila) % n
            vector[columna] = new_value
            if vector not in blacklist:
                offspring_states.append(vector)#agregamos el nuevo decendiente

            vector = copy.copy()

    return offspring_states


def evaluate(offsprings):#unicamente obtiene los ataques de cada nodo
    number_attacks = []#crea una lista
    for child in offsprings:
        number_attacks.append(attacks(child)) #los ataques de cada hijo

    return number_attacks


# Bubble Sort
def bubble_sort(offsprings, attacks):
    swapped = False

    for n in range(len(attacks) - 1, 0, -1):
        for i in range(n):
            if attacks[i] > attacks[i + 1]:
                swapped = True
                attacks[i], attacks[i + 1] = attacks[i + 1], attacks[i]
                offsprings[i], offsprings[i + 1] = offsprings[i + 1], offsprings[i]
        if not swapped:
            break

    return offsprings


def attacks(vector):#en este metodo obtenemos la cantidad de ataques
    attacks = 0

    for i in range(1, n):  # for i = 1; i < n; i++
        for j in range(i + 1, n + 1):  # for j = i+1; j <= n; j++
            if vector[i - 1] == vector[j - 1]:
                attacks += 2
            if abs(i - j) == abs(vector[i - 1] - vector[j - 1]):
                attacks += 2

    return attacks


def print_board(board: list[int]): # metodo de impresion del tablero
    print_hline("┌", "───┬", "┐", len(board))
    for j in range(len(board)):
        for i in range(len(board)):
            print("│ X ", end="") if board[i] == j else print("│   ", end="")
        print("│")
        print_hline("├", "───┼", "┤", len(board)) if j != len(board) - 1 else print_hline("└", "───┴", "┘", len(board))


def print_hline(first: str, middle: str, last: str, size: int):
    line: str = first
    line += middle * size
    print(line[0:-1] + last)


###########
def main():
    print("# Calculemos el tablero para ", n, " reinas #")
    greedys(f)


if __name__ == "__main__":
    main()