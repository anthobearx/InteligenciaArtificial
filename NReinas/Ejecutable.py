from Datos import ciudades_de_romania, a_estrella, ruta_tostring, tabla_distancia_lineal
from Grafico import graph

def main():
    print("ciudades romanisticas")
    tazo = True
    while tazo:
        try:
            origen = str(input(" Ciudad de origen: "))
        except:
            tazo = True
        if origen in tabla_distancia_lineal:
            tazo = False

    cd_inicial = ciudades_de_romania(origen) # se obtiene la cd actual
    f = []#creacion de f como una lista
    f.append(cd_inicial) #
    imp, meta = a_estrella(f) #se imprime y se da la meta conseguida
    print("\n" + imp + ": " + ruta_tostring(meta) + "\n")
    graph(meta)#aqui graficamos el mapa


if __name__ == "__main__":
    main()