#(ataque([3,1,4,2])) sin ataques

def ataque(reinas):
    n = len(reinas)
    ataques = 0

    for i in range(n): #for que itera el numero de veces que mide el arreglo enviadO
        for j in range(i+1,n):
            if reinas[i] == reinas[j]:
                ataques+=2
            if abs(i - j) == abs(reinas[i] - reinas[j]):
                ataques+=2
    return ataques

#goaltest = encontrar la manera en la que ataques = 0, y si es igual a 0, añadirlo a una lista de
#listas pasables
#def goaltest():


#def expand():


#primero necesito de un arreglo inicial
#edo_objetivo --> ataques = 0 ---> goaltest ==true ---> añadir a listas de listas
#me imagino que ingresamos n, para la cantidad de tableros y reinas que abra,
#con esto preguntaria si es goaltest, en el que goaltest ataques ==0
#si es goaltest, añadirlo a soluciones, si no, continuar con el expand



def reinas(n: int): #recibe un numero
    tablero = [1]*n #crea un arreglo de 1 del tamaño solicitado
    print(tablero)
    if goalTest(tablero):
        print("Tablero encontrado:")
        print(tablero)
        return



# Lee un número entero desde el teclado y lo almacena en una variable
entrada = input("¿De que la longitud sera el tablero?")
n = int(entrada)
reinas(n)




#print(ataque([3,1,4,2]))