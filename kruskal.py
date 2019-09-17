import time

def imprime_arvore_geradora_minima(arvore, grafoOrigem):
    print("\n==============================================\n")
    peso = 0
    for tupla in arvore:
        # print("|", tupla[0], "|", tupla[1], "| - ", grafoOrigem[tupla[0]][tupla[1]])
        peso = peso + grafoOrigem[tupla[0]][tupla[1]]
    print('Peso da árvore geradora mínima (Kruskal): ', peso)

def quicksort(vetor,inicio,fim, grafo_inteiro):
    if(inicio < fim):
        limites = sort(vetor,inicio,fim, grafo_inteiro) # limites[0] = pivô; limites[1] = inicio; limites[2] = fim
        quicksort(vetor, limites[1], limites[0]-1, grafo_inteiro) #(vetor, inicio, pivo-1, grafo)
        quicksort(vetor, limites[0]+1, limites[2], grafo_inteiro) #(vetor, pivo+1, fim, grafo)

def sort(vetor, inicio,fim, grafo_inteiro):
    pivo = vetor[fim]
    contador = inicio-1

    for posicao in range(inicio,fim):
        distVetor = distancia(grafo_inteiro, vetor[posicao])
        distPivo = distancia(grafo_inteiro, pivo)
        if( distVetor <= distPivo):
            contador += 1
            vetor[contador],vetor[posicao] = vetor[posicao],vetor[contador]

    vetor[contador+1],vetor[fim] = vetor[fim],vetor[contador+1]
    return contador+1,inicio,fim

def distancia(grafo, aresta):
    # Checa peso de dois nós ou arestas
    origem = aresta[0]
    destino = aresta[1]
    for item in grafo[origem]:
        if item == destino:
          distancia = grafo[origem][item]
    return distancia

def ordena_arestas(grafo_inteiro):
    arestas_ordenadas = []
    # Armazenar tuplas de nos ordenadas de acordo com o peso
    for chave ,vizinhos in grafo_inteiro.items():
        for vizinho in vizinhos:
            arestas_ordenadas.append(tuple([chave, vizinho]))
    quicksort(arestas_ordenadas, 0, len(arestas_ordenadas)-1, grafo_inteiro) # Vetor de tuplas de nós, inicio, fim, grafo
    return arestas_ordenadas

# Criando tabela inicial
tabela = {}

def montar_tabela(aeroportos):
    tabela[aeroportos] = set([aeroportos]) # Setando aeroportos para cada aeroporto

def encontrar(aeroporto):
    for origem , destinos in tabela.items():
        if aeroporto in destinos: # Se aeroporto estiver nos destinos databela
            return origem
    return None

def unir(arvore_x, arvore_y):
    origem_arvore_x = encontrar(arvore_x)
    origem_arvore_y = encontrar(arvore_y)
    tabela[origem_arvore_y] = tabela[origem_arvore_y].union(tabela[origem_arvore_x])
    del tabela[origem_arvore_x]

def kruskal(grafo):
    # Ordenar arestas em ordem crescente de custos para selecionar os de menor custo em O(1)
    arestas_ordenadas = ordena_arestas(grafo)
    arvore_geradora_minima = [] # Setando arvore geradora mínima como vetor vazio

    #Para os destinos na lista de origens (chaves)
    for destinos in grafo.keys():
        montar_tabela(destinos)
    for aresta in arestas_ordenadas: # Para cada aresta testa se pertencem à mesma árvore
        if encontrar(aresta[0]) != encontrar(aresta[1]):
            arvore_geradora_minima.append(aresta)
            unir(aresta[0], aresta[1])

    return arvore_geradora_minima

def kruskal_algoritmo(listaDeAdjacencia):
    start = time.time()
    arvore_geradora_minima = kruskal(listaDeAdjacencia)
    end = time.time()
    imprime_arvore_geradora_minima(arvore_geradora_minima, listaDeAdjacencia)
    print('Tempo decorrido: ', end - start)
