import tablero as tablib
#caracteres utilizados en el tablero
#primero
primero = "┌"
segundo = "───┬"
tercero = "┐"
#abajo
cuarto = "├"
quinto = "───┼"
sexto = "┤"
#para final
septimo = "└"
octavo = "───┴"
noveno = "┘"


def print_tablero(tablero: tablib.tablero) -> None:#lineas verticales
    #print_h_tablero(primero, segundo, tercero, tablero.tamano)
    tamano = tablero.tamano
    linea: str = primero
    linea += segundo * tamano
    print(linea[0:-1] + tercero)
    for j in range(tablero.tamano):
        for i in range(tablero.tamano):
            print("│ X ", end="") if tablero.reinas[i] == j else print("│   ", end="")
        print("│")
        linea: str = cuarto
        linea += quinto * tamano
        print(linea[0:-1] + sexto)
        if not (j != tablero.tamano - 1):
            print()

def main() -> None:
    print("\n== Reinas==\n")

    tazo = True
    while tazo:
        try:
            tamano = int(input("Tamaño del tablero: "))#de preferencia 4
            tazo = False
        except:
            tazo = True
    print("\nAlgoritmos de búsqueda:\n" +
          "\n" +
          "--- (Máximo 5 reinas) ---\n" +
          "  1.- Busqueda anchura \n" +
          "  2.- Busqueda profunda\n" +
          "  3.- Busqueda limitada\n" +
          "  4.- Busqueda iterada\n" +
          "\n" +
          "--- (Probado hasta 50 reinas)---\n" +
          "  5.- Busqueda Voraz\n" +
          "\n" +
          "  0.- Salir")
    tazo = True
    while tazo:
        try:
            opcion = int(input("Selecciona el algoritmo: "))
            if opcion >= 0 and opcion <= 5:
                tazo = False
        except:
            tazo = True
    print()

    visitado = []#se manda como parametro
    partida = tablib.tablero(visitado=visitado, tamano=tamano)
    frontera = [] #lista
    frontera.append(partida)
    if opcion == 1:
        mensaje, meta = tablib.bf_s(frontera)#Busqueda anchura
    elif opcion == 2:
        mensaje, meta = tablib.df_s(frontera)#Busqueda profunda
    elif opcion == 3: #Busqueda limitada
        tazo = True
        while tazo:
            try:
                limite = int(input(" Ingresa el limite: "))
                if limite > 0:
                    tazo = False
            except:
                tazo = True
        mensaje, meta = tablib.dl_s(frontera, limite)
    elif opcion == 4:  #Busqueda iterada
        tazo = True
        while tazo:
            try:
                incremento = int(input(" Ingresa el incremento: "))#checar eso del incremento
                if incremento > -1:
                    tazo = False
            except:
                tazo = True
        mensaje, meta = tablib.idl_s(partida, 2, incremento)
    elif opcion == 5:
        mensaje, meta = tablib.g_s(frontera)

    print(mensaje)
    if meta != None: print_tablero(meta)

    print("\nSe acabo...\n")


if __name__ == "__main__":
    main()