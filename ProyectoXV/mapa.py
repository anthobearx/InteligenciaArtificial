import matplotlib.pyplot as plt
import networkx as nx
from algoritmoAEstrella import claseciudad, lista_de_rutas


class punto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


G = nx.Graph()
ciudades_grafo = ['Amsterdam', 'Berlin', 'Bruselas', 'Budapest', 'Copenhague', 'Madrid', 'Paris', 'Praga', 'Roma', 'Varsovia',
         'Viena', 'Zurich']

rutas_grafo = [#de donde a donde se puede ir
    ('Amsterdam', 'Bruselas'), ('Amsterdam', 'Zurich'), ('Amsterdam', 'Berlin'),
    ('Berlin', 'Praga'), ('Berlin', 'Varsovia'), ('Berlin', 'Copenhague'),
    ('Bruselas', 'Paris'),
    ('Budapest', 'Viena'), ('Budapest', 'Varsovia'),
    ('Madrid', 'Paris'), ('Madrid', 'Zurich'),
    ('Praga', 'Viena'),('Praga', 'Zurich'),
    ('Roma', 'Zurich'),
    ('Varsovia', 'Viena')
]

coordenadas_grafo = {#con estas se grafican en el grafo
    'Amsterdam': (541, 271),
    'Berlin': (711, 261),
    'Bruselas': (528, 250),
    'Budapest': (865, 160),
    'Copenhague': (793, 298),
    'Madrid': (470, 110),
    'Paris': (506, 218),
    'Praga': (738, 216),
    'Roma': (676, 110),
    'Varsovia': (860, 260),
    'Viena': (812, 167),
    'Zurich': (620, 176)
}

#añade la informacion al grafo
G.add_nodes_from(ciudades_grafo)
G.add_edges_from(rutas_grafo)

#metodo que lo pinta
def graficarGrafo(claseciudad: claseciudad) -> None:
    nx.draw(G, pos=coordenadas_grafo, node_color='gray', edge_color='black', with_labels='true')  # Dibujamos todo el grafo

    nodes = lista_de_rutas(claseciudad)
    edges_route = []
    for i in range(len(nodes) - 1):
        edges_route.append((nodes[i], nodes[i + 1]))
    GR = nx.Graph()
    GR.add_nodes_from(nodes[1:-2])
    GR.add_edges_from(edges_route)
    nx.draw(GR, pos=coordenadas_grafo, node_color='blue', edge_color='blue', with_labels='true')  # Dibujamos el recorrido
    GR = nx.Graph()
    GR.add_node(nodes[-1])
    nx.draw(GR, pos=coordenadas_grafo, node_color='purple', with_labels='true')  # Dibujamos el origen
    GR = nx.Graph()
    GR.add_node(nodes[0])
    nx.draw(GR, pos=coordenadas_grafo, node_color='red', with_labels='true')  # Dibujamos el destino (goaltest)

    plt.show()
