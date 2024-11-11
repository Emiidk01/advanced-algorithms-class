import sys

def prim_mst(graph, n):
    """
    Encuentra el Arbol de Expansión Mínima (MST) usando el algoritmo de Prim.

    Parametros:
        graph (lista de listas): Matriz de adyacencia que representa el grafo.
        n (int): Numero de nodos en el grafo.

    Devuelve:
        tuple: Una lista de aristas en el MST (lista de tuplas) y el costo total del MST (int).

    Complejidad:
        O(n^2) - Debido a la doble iteracion sobre los nodos y la busqueda de aristas de menor peso.
    """
    selected_node = [False] * n
    selected_node[0] = True
    mst_edges = []
    total_cost = 0

    for _ in range(n - 1):
        min_weight = sys.maxsize
        a = b = -1

        for u in range(n):
            if selected_node[u]:
                for v in range(n):
                    if not selected_node[v] and graph[u][v] > 0:
                        if graph[u][v] < min_weight:
                            min_weight = graph[u][v]
                            a, b = u, v

        if a != -1 and b != -1:
            mst_edges.append((a, b))
            total_cost += min_weight
            print(total_cost)
            selected_node[b] = True

    return mst_edges, total_cost

# lectura de la matriz de adyacencias desde un archivo
def leer_matriz_adyacencia(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for _ in range(n):
            fila = list(map(int, f.readline().strip().split()))
            graph.append(fila)
    return n, graph

# uso
nombre_archivo = "input.txt"
n, graph = leer_matriz_adyacencia(nombre_archivo)
mst_edges, total_cost = prim_mst(graph, n)
print("Aristas del MST:", mst_edges)
print("Costo total de fibra óptica:", total_cost)
