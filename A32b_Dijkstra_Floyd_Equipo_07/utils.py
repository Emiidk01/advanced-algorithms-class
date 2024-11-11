import heapq

INF = float('inf')

"""
Creado en: 20/10/2024
Actualizado en: 20/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711
Función de Dijkstra

Descripción: Esta función implementa el algoritmo de Dijkstra para encontrar las distancias mínimas
desde un nodo de inicio 'start' a todos los demás nodos en un grafo representado como una matriz de adyacencia.

Parámetros:
start: el índice del nodo de inicio.
graph: una matriz de adyacencia donde graph[u][v] es el peso de la arista de u a v, o -1 si no hay arista.

Complejidad: O((V + E) log V), donde V es el número de nodos y E el número de aristas. Esto se debe al uso de
una cola de prioridad (priority queue) implementada con heapq
"""
def dijkstra(start, graph):
    n = len(graph)
    dist = [INF] * n # Inicializar distancias a infinito
    dist[start] = 0
    
    pq = [(0, start)]  # priority queue, (distancia, nodo)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v in range(n):
            if graph[u][v] != -1:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    for i in range(n):
        if i != start:
            if dist[i] == INF:
                print(f"node {start + 1} to node {i + 1}: INF")
            else:
                print(f"node {start + 1} to node {i + 1}: {dist[i]}")


"""
Función de Floyd-Warshall

Descripción: Esta función implementa el algoritmo de Floyd-Warshall para encontrar las distancias mínimas
entre todos los pares de nodos en un grafo. El grafo se representa como una matriz de adyacencia.

Parámetros:
graph: una matriz de adyacencia donde graph[u][v] es el peso de la arista de u a v, o -1 si no hay arista.

Complejidad: O(V^3), donde V es el número de nodos. Este algoritmo es más adecuado para grafos densos
o cuando necesitamos las distancias entre todos los pares de nodos.
"""
def floyd_warshall(graph):
    n = len(graph)
    # Inicializar la matriz de distancias. Si no hay arista, la distancia es infinita
    dist = [[graph[i][j] if graph[i][j] != -1 else INF for j in range(n)] for i in range(n)]

    # Actualizamos las distancias considerando cada nodo como posible intermediario
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print("Floyd:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
