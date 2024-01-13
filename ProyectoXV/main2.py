def a_estrella():
    print("ejecutando a*")
    ciudadinicial = claseciudad(combo_ciudades.get())  # ciudad inicial, declarada como claseciudada
    print("la ciudad para iniciar es: ", ciudadinicial.nombre_ciudad)
    frontier:list[claseciudad] = []#lista frontier es lista de tipo claseciudad
    frontier.append(ciudadinicial)  # Se agrega a la frontera
    solucion, meta = aestrella(frontier)  # Llamanos a la función de búsqueda y recibimos un mensaje y la ciudad destino con la ruta recorrida
    print("\n" + solucion + ": " + rutasAEstrella(meta) + "\n")
    graficarGrafo(meta)
    print("----------------------------------------------------")