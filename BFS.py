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
            if not largura.get(vizinho):
                fila.append(vizinho)
                ctdLargura += 1
                largura[vizinho] = ctdLargura
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1
                if vizinho == aeroporto_destino:
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
