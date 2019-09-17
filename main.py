import pandas as pd
import json
from math import radians, cos, sin, asin, sqrt
from prim import *
from kruskal import *
from dijkstra import *

listaDeAdjacencia = {}

# Formula de Haversine
def haversine( a, b ):
    # Raio da Terra em Km
    r = 6371

    # Converte coordenadas de graus para radianos
    lon1, lat1, lon2, lat2 = map(radians, [ a['longitude'], a['latitude'], b['longitude'], b['latitude'] ] )

    # Formula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    d = 2 * r * asin( sqrt(hav) )

    return d

def main():

    pd.read_csv('VoosAzul.csv').to_json('VoosAzul.json')

    with open('VoosAzul.json') as json_file:
        data = json.load(json_file)

    # Montando lista de adjacência
    for (key, aeroporto) in data['Aeroporto.Origem'].items():
        if not listaDeAdjacencia.get(aeroporto):
            listaDeAdjacencia[aeroporto] = {}

        cordOrigem = {'latitude': data['LatOrig'][key], 'longitude': data['LongOrig'][key]}
        cordDestino = {'latitude': data['LatDest'][key], 'longitude': data['LongDest'][key]}

        listaDeAdjacencia[aeroporto][data['Aeroporto.Destino'][key]] = haversine(cordOrigem, cordDestino)

    # Salvando lista de adjacência
    with open('listaAdjacência.json', 'w') as json_file:
        json.dump(listaDeAdjacencia, json_file)


graph = {
    'a': {'b': 4, 'c': 4},
    'b': {'a': 4, 'c': 2},
    'c': {'a': 4, 'd': 3, 'e': 4, 'f': 2},
    'd': {'c': 3, 'e': 3},
    'e': {'c': 4, 'd': 3, 'f': 3},
    'f': {'c': 2, 'e': 3}
}

# print(listaDeAdjacencia)
main()
qtd_nos = len(listaDeAdjacencia)
print("\n\n==========================\nNúmero de aeroportos: ", qtd_nos, "\n==========================\n")

prim_algoritmo(listaDeAdjacencia)
kruskal_algoritmo(listaDeAdjacencia)
dijkstra(listaDeAdjacencia, "Hercilio Luz", "Carajas")
