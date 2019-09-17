def dijkstra(grafo,origem,destino,visitados=[],distancia={},predecessor={}):
    """ calculates a shortest path tree routed in origem
    """
    if origem not in grafo:
        raise TypeError('O aeroporto de origem não pôde ser encontrado')
    if destino not in grafo:
        raise TypeError('O aeroporto de destino não pôde ser encontrado')
    if origem == destino:
        # Construindo o caminho mais curto
        caminho = []
        pred = destino
        while pred != None:
            caminho.append(pred)
            pred = predecessor.get(pred, None)
        # reverte o array
        emprimirCaminho = caminho[0]
        for index in range(1, len(caminho)):
            emprimirCaminho = caminho[index] + ' ---> ' + emprimirCaminho

        print("\n==============================================\n")
        print("Dijkstra")
        print("Caminho mais curto: "+ emprimirCaminho + ",\ncusto=" + str(distancia[destino]))
    else :
        # Se nunca foi calculado, inicializa o custo
        if not visitados:
            distancia[origem] = 0
        # Visita os vizinhos
        for vizinho in grafo[origem] :
            if vizinho not in visitados:
                novaDistancia = distancia[origem] + grafo[origem][vizinho]
                if novaDistancia < distancia.get(vizinho, float('inf')):
                    distancia[vizinho] = novaDistancia
                    predecessor[vizinho] = origem
        # Marca como vizitado
        visitados.append(origem)
        # now that all vizinhos have been visitados: recurse
        # select the non visitados node with lowest distance 'x'
        # run Dijskstra with origem='x'
        naoVisitados={}
        for k in grafo:
            if k not in visitados:
                naoVisitados[k] = distancia.get(k, float('inf'))
        x = min(naoVisitados, key=naoVisitados.get)
        dijkstra(grafo, x, destino, visitados, distancia, predecessor)
