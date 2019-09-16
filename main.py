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

#print(listaDeAdjacencia)
# Pegar número de aeroportos     
qtd_nos = len(listaDeAdjacencia)

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
#print(imprime_menor_caminho(pai, "Adalberto Mendes Da Silva", "Porto Seguro"))

def quicksort(vetor,inicio,fim, grafo_inteiro):
    if(inicio < fim):
        limites = sort(vetor,inicio,fim, grafo_inteiro) # limites[0] = pivô; limites[1] = inicio; limites[2] = fim
        quicksort(vetor, limites[1], limites[0]-1, grafo_inteiro) #(vetor, inicio, pivo-1, grafo)        
        quicksort(vetor, limites[0]+1, limites[2], grafo_inteiro) #(vetor, pivo+1, fim, grafo)

def sort(vetor, inicio,fim, grafo_inteiro):
    pivo = vetor[fim]
    contador = inicio-1   

    for posicao in range(inicio,fim):
        if(distancia(grafo_inteiro, vetor[posicao]) <= distancia(grafo_inteiro, pivo)):
            contador += 1
            vetor[contador],vetor[posicao] = vetor[posicao],vetor[contador]

    vetor[contador+1],vetor[fim] = vetor[fim],vetor[contador+1]
    return contador+1,inicio,fim

def distancia(grafo, aresta):
    # Checa peso de dois nós ou arestas
    origem = aresta[0]
    destino = aresta[1]
    for item in grafo[origem]:
        if item[0] == destino:
          distancia = item[1]
    return distancia

def ordena_arestas(grafo_inteiro):
    arestas_ordenadas = []

    # Armazenar tuplas de nos ordenadas de acordo com o peso
    for chave ,vizinhos in grafo_inteiro.items():
        for vizinho, peso in vizinhos:
            arestas_ordenadas.append(tuple([chave, vizinho]))
    quicksort(arestas_ordenadas, 0, len(arestas_ordenadas)-1, grafo_inteiro) # Vetor de tuplas de nós, inicio, fim, grafo
    return arestas_ordenadas

# Criando tabela inicial
tabela = {}

def montar_tabela(aeroportos):
    tabela[aeroportos] = set([aeroportos]) # Setando aeroportos para cada aeroporto

def encontrar(aeroporto):
    for origem , destinos in tabela.items():
        # print("Origem: ", origem, "Destinos: ", destinos) 
        if aeroporto in destinos: # Se aeroporto estiver nos destinos databela 
            return origem
    return None

def unir(x, y):
    xRepresentative = encontrar(x)
    yRepresentative = encontrar(y)
    tabela[yRepresentative] = tabela[yRepresentative].union(tabela[xRepresentative])
    del tabela[xRepresentative]

def kruskal(grafo):
    # Ordenar arestas em crescente para selecionar os de menor custo
    arestas_ordenadas = ordena_arestas(grafo)

    arvore_geradora_minima = [] # Setando arvore geradora mínima como vetor vazio
    
    #Para os destinos na lista de origens (chaves)
    for destinos in grafo.keys():
        montar_tabela(destinos)
    for aresta in arestas_ordenadas: # Para cada aresta testa se pertencem à mesma árvore
        if encontrar(aresta[0]) != encontrar(aresta[1]): # Se for de arvores diferentes adiciona na árvore geradora mínima
            # print("Aresta 0", aresta[0], "Aresta 1:", aresta[1])
            arvore_geradora_minima.append(aresta)
            unir(aresta[0], aresta[1])

    return arvore_geradora_minima

def kruskal_algoritmo(listaDeAdjacencia):
    qtd_nos = len(listaDeAdjacencia)

    arvore_geradora_minima = kruskal(listaDeAdjacencia)
    print(arvore_geradora_minima)

kruskal_algoritmo(listaDeAdjacencia)
