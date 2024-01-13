import tkinter as tk #libreria para graficar
from tkinter import ttk
import random
from algoritmoAEstrella import claseciudad, aestrella, rutasAEstrella
from mapa import graficarGrafo
from permutaciones import rutaOptima, rutasPermutadasToString, imprimirPermutaciones
from google import graficarMaps

# Aqui se guardan las 12 ciudades
capitales = [
    "Amsterdam", "Berlin", "Bruselas", "Budapest", "Copenhague", "Madrid", "Paris", "Praga", "Roma", "Varsovia",
    "Viena", "Zurich"  # Aunque Zúrich no es la capital, es una ciudad principal
]

#metodos o eventos

#actualiza el combobox con las ciudades que esten seleccionados en el checklist
def actualizar_combobox():
    ciudades_seleccionadas = [ciudad for ciudad, var in checkboxes.items() if var.get()]
    combo_ciudades['values'] = ciudades_seleccionadas#se obtienen los valores seleccionados en el combo


#cuando seleccionas una de las 8 ciudades en el combo box, se ejecuta este evento
def seleccionar_ciudad(event):
    ciudad = combo_ciudades.get()
    label_resultado.config(text=f"La ciudad inicial es: {ciudad}")

def seleccionar_aleatorias():#metodo de seleccion aleatoria de 8 ciudades
    for ciudad, var in checkboxes.items():#ponerlas todos en falso
        var.set(False)
    ciudades_aleatorias = random.sample(capitales, 8)#elegir 8 checkboxes aleatorios
    for ciudad in ciudades_aleatorias:
        checkboxes[ciudad].set(True)#los poner en verdadero a esas 8 ciudades
    actualizar_combobox()#actualiza
    #poner la primera ciudad en el combobox
    if (len(combo_ciudades['values'])>1):#si es aleatorio, que la ciudad de inicio sea la primera del combo box
        combo_ciudades.set(combo_ciudades['values'][0])
        ciudad = combo_ciudades.get()
        label_resultado.config(text=f"La ciudad inicial es: {ciudad}")



#limpia cada uno de los checkboxes elegidos, y actualiza el combobox
def limpiar_seleccion():
    for var in checkboxes.values():
        var.set(False)#pone todos en falso
    actualizar_combobox()
def calcular():#pulsar el boton calcular, ejecuta aqui
   #comprobar que sean 8 ciudades y tenga una ciudad de inicio
    if ( len(combo_ciudades['values']) != 8 or combo_ciudades.get() == ""):
        print("Debes elegir 8 ciudades y una ciudad inicio")
    else:
       ciudadInicial = combo_ciudades.get()
       ciudades_por_visitar = combo_ciudades['values']#guardamos las 8 ciudades en ciudades x visitar
       ciudades_por_visitar = removerCiudad(ciudadInicial, ciudades_por_visitar)#quitamos la ciudad de inicio
       rutaEuropa, distancia = rutaOptima(ciudadInicial, ciudades_por_visitar)  # Llamamos al método de viaje más corto
       print(f'Ruta: {rutasPermutadasToString(rutaEuropa)}\n\nDistancia a recorrer: {str(distancia)} km')

       #print("Todas las rutas:")
       #imprimirPermutaciones(ciudadInicial,ciudades_por_visitar) #imprime todas las posibilidades

       print("Generando mapa...")
       graficarMaps(rutaEuropa)





#recibe una lista y una ciudad, quita esa ciudad de esa lista
def removerCiudad(ciudad, listaciudad):
    listaciudad = list(listaciudad)  # Convertir la tupla a lista
    if ciudad in listaciudad:  # Quitar solo si es parte de la lista
        listaciudad.remove(ciudad)
    return listaciudad


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

# Configuración de la ventana principal
root = tk.Tk()
root.title("Selector de Ciudades Capitales Europeas")#titulo

# Definir la fuente a utilizar
font_style = ("Century Gothic", 10)

# Creación de los checkboxes
checkboxes = {}
for i, ciudad in enumerate(capitales):#se usa un for que repasa la lista de capitales y crea sus respectivos checkboxes
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=ciudad, variable=var, command=actualizar_combobox)#se agrega el comando
    #chk.pack()#se colocan
    # Usa grid para organizar los checkboxes en dos columnas
    chk.grid(row=i // 2, column=i % 2, sticky="w")
    checkboxes[ciudad] = var

# Etiqueta para instrucciones
label_instrucciones = tk.Label(root, text="Selecciona solo 8 ciudades", font=font_style)
label_instrucciones.grid(row=0, column=2, columnspan=2)

# Creación del Combobox
combo_ciudades = ttk.Combobox(root, state="readonly", font=font_style)
combo_ciudades.bind('<<ComboboxSelected>>', seleccionar_ciudad)
combo_ciudades.grid(row=7, column=0, columnspan=4, pady=5)

# Botones
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_seleccion, font=font_style)
btn_limpiar.grid(row=1, column=2, sticky="e")

btn_aleatorio = tk.Button(root, text="Aleatorio", command=seleccionar_aleatorias, font=font_style)
btn_aleatorio.grid(row=2, column=2, sticky="e")

btn_calcular = tk.Button(root, text="Calcular viaje", command=calcular, font=font_style)  # Sin comando aún
btn_calcular.grid(row=3, column=2, sticky="e")

btn_tablas = tk.Button(root, text="A*", command=a_estrella, font=font_style)  # Sin comando aún
btn_tablas.grid(row=4, column=2, sticky="e")

# Etiqueta para mostrar la ciudad seleccionada
label_resultado = tk.Label(root, text="Selecciona una ciudad para empezar", font=font_style)
label_resultado.grid(row=6, column=0, columnspan=4)

# Iniciar la aplicación
root.mainloop()
