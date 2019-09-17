from collections import defaultdict
import heapq
import time

def imprime_arvore_geradora_minima(arvore, grafoOrigem):
    print("\n==============================================\n")
    peso = 0
    for origem in arvore:
        for destino in arvore[origem]:
            peso = peso + grafoOrigem[origem][destino]
    print('Peso da árvore geradora mínima (Prim): ', peso)

def prim(graph):
    starting_vertex = list(graph)[0]
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

def prim_algoritmo(listaDeAdjacencia):
    start = time.time()
    arvore_geradora_minima = prim(listaDeAdjacencia)
    end = time.time()
    imprime_arvore_geradora_minima(arvore_geradora_minima, listaDeAdjacencia)
    print('Tempo decorrido: ', end - start)
