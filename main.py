import pandas as pd
pd.read_csv('VoosAzul.csv').to_json('VoosAzul.json')

from math import radians, cos, sin, asin, sqrt

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


AdalbertoMendesDaSilva = {'latitude': -25.001815, 'longitude': -53.501918 }
Viracopos = {'latitude': -23.008205, 'longitude': -47.1375685}

print("Adalberto x Viracopos: " + str( haversine( AdalbertoMendesDaSilva, Viracopos) ) + " Km")

import json

with open('VoosAzul.json') as json_file:
    data = json.load(json_file)

# print(data)
listaDeAdjacencia = {}

# Montando lista de adjacência
for (key, aeroporto) in data['Aeroporto.Origem'].items():
    if not listaDeAdjacencia.get(aeroporto):
        listaDeAdjacencia[aeroporto] = []

    cordOrigem = {'latitude': data['LatOrig'][key], 'longitude': data['LongOrig'][key]}
    cordDestino = {'latitude': data['LatDest'][key], 'longitude': data['LongDest'][key]}

    listaDeAdjacencia[aeroporto].append([data['Aeroporto.Destino'][key], haversine(cordOrigem, cordDestino)])


# Salvando lista de adjacência
with open('listaAdjacência.json', 'w') as json_file:
    json.dump(listaDeAdjacencia, json_file)

print(listaDeAdjacencia)

def BFS(grafo, aeroporto_origem, aeroporto_destino):
    fila = []
    visitados = []
    largura = {}
    ctdLargura = 1
    nivel = {}
    pai = {}

    fila.append(aeroporto_origem)
    largura[aeroporto_origem] = ctdLargura
    nivel[aeroporto_origem] = 1
    pai[aeroporto_origem] = None

    while len(fila):
        vertice = fila.pop(0)

        for vizinho in grafo.get(vertice):
            if not largura.get(vizinho[0]):
                fila.append(vizinho[0])
                ctdLargura += 1
                largura[vizinho[0]] = ctdLargura
                pai[vizinho[0]] = vertice
                nivel[vizinho[0]] = nivel[vertice] + 1
                if vizinho[0] == aeroporto_destino:
                    return largura, nivel, pai
    return 0

def imprime_menor_caminho(pai, aeroporto_origem, aeroporto_destino):
    menor_caminho = []
    while aeroporto_destino != aeroporto_origem:
        menor_caminho.insert(0, aeroporto_destino)
        aeroporto_destino = pai[aeroporto_destino]

    menor_caminho.insert(0, aeroporto_origem)
    return menor_caminho

largura, nivel, pai = BFS(listaDeAdjacencia, "Adalberto Mendes Da Silva", "Porto Seguro")
print(imprime_menor_caminho(pai, "Adalberto Mendes Da Silva", "Porto Seguro"))
