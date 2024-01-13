import googlemaps
import gmplot
from datetime import datetime

#idea de api de google maps con javascript, descartada (no tengo tiempo ni ganas de aprender js xd)
#idea 2: buscar libreria para graficar las coordenadas
#capitales = [
#    "Amsterdam", "Berlin", "Bruselas", "Budapest", "Copenhague", "Madrid", "Paris", "Praga", "Roma", "Varsovia",
#    "Viena", "Zurich"  # Aunque Zúrich no es la capital, es una ciudad principal
#]

gmaps = googlemaps.Client(key='AIzaSyDDxJYDteF6jpU2qsQZ6As8ErusMkUaFTI')

# Obtener latitud y longitud de una ciudad
# geocode_result = gmaps.geocode('Zurich')
# print(geocode_result[0]["formatted_address"])
# print(geocode_result[0]["geometry"]["location"]["lat"])
# print(geocode_result[0]["geometry"]["location"]["lng"])

#def graficarMaps(localizaciones):
#    markers = ["color:blue|size:mid|label:" + chr(65 + i) + "|"
#               + r for i, r in enumerate(localizaciones)]
#
#    result_map = gmaps.static_map(
#        center=localizaciones[0],#inicio
#        scale=2,
#        zoom=12,
#        size=[640, 640],
#        format="jpg",
#        maptype="roadmap",
#        markers=markers,
#        path="color:0x0000ff|weight:2|" + "|".join(localizaciones))


def graficarMaps(localizaciones):
    # Obtén las coordenadas geográficas de cada ciudad
    coordenadas = [gmaps.geocode(ciudad)[0]['geometry']['location'] for ciudad in localizaciones]

    # Extrae la ciudad de origen y destino
    ciudad_origen = coordenadas[0]#la primera ciudad
    ciudad_destino = coordenadas[-1]#la ultima

    # Todas las ciudades intermedias serán waypoints
    waypoints = coordenadas[1:-1]

    # Usa la API de direcciones para obtener la ruta
    direcciones = gmaps.directions(ciudad_origen,
                                   ciudad_destino,
                                   mode="driving",
                                   waypoints=waypoints,
                                   avoid=['ferries', 'highways'], #evitar ferries y autopistas largas
                                   optimize_waypoints=False,  # Si utilizamos true, puede que cambie el orden (aunque no deberia)
                                   departure_time=datetime.now())

    # Aquí puedes trazar la ruta con gmplot o la herramienta que prefieras
    # Extraer puntos de la ruta
    latitudes = []
    longitudes = []

    # Iterar sobre los resultados de las direcciones y extraer las latitudes y longitudes
    for leg in direcciones[0]['legs']:
        for step in leg['steps']:
            latitudes.append(step['start_location']['lat'])
            longitudes.append(step['start_location']['lng'])
            # Añadir un marcador en cada paso de la ruta
        latitudes.append(leg['end_location']['lat'])
        longitudes.append(leg['end_location']['lng'])



    # Crear un objeto gmplot y centrarlo en la primera ubicación de la ruta
    gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 3)

    # Traza la ruta en el mapa
    gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=3)

    # Añadir marcadores para cada ciudad
    for coordenada in coordenadas:
        gmap.marker(coordenada['lat'], coordenada['lng'], 'red')

    # Guardar el mapa en un archivo HTML
    gmap.draw("ruta_mapa2.html")

    #file:///C:/Users/Antho/PycharmProjects/mainQuincea%C3%B1eras/ruta_mapa.html
    #C:\Users\antho\PycharmProjects\mainQuinceañeras




