from collections import deque
import math
from heapq import heappop, heappush

# Función para obtener el Árbol de Expansión Mínima (Kruskal)
def kruskal_mst(adj_matrix):
    n = len(adj_matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] > 0:
                edges.append((adj_matrix[i][j], i, j))
    edges.sort()

    parent = list(range(n))
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_edges, mst_weight


def tsp_dp(adj_matrix):
    n = len(adj_matrix)
    dp = [[float('inf')] * (1 << n) for _ in range(n)]  # DP table
    dp[0][1] = 0  # Start at city 0

    # Llenar la tabla dp con costos mínimos para cada subconjunto de ciudades
    for mask in range(1, 1 << n):
        for u in range(n):
            if (mask >> u) & 1:  # Si u está en el subconjunto representado por mask
                for v in range(n):
                    if (mask >> v) & 1 == 0:  # Si v no está en el subconjunto
                        dp[v][mask | (1 << v)] = min(dp[v][mask | (1 << v)], dp[u][mask] + adj_matrix[u][v])

    # Encontrar el último nodo de la ruta óptima y el costo mínimo
    min_cost = float('inf')
    last_node = -1
    for i in range(1, n):
        if dp[i][(1 << n) - 1] + adj_matrix[i][0] < min_cost:
            min_cost = dp[i][(1 << n) - 1] + adj_matrix[i][0]
            last_node = i

    # Recuperar la ruta óptima sin repeticiones
    tsp_route = []
    mask = (1 << n) - 1
    for _ in range(n - 1):  # Recorrer n-1 ciudades además del inicio
        tsp_route.append(last_node)
        next_node = -1
        for i in range(n):
            if (mask >> i) & 1 and dp[last_node][mask] == dp[i][mask ^ (1 << last_node)] + adj_matrix[i][last_node]:
                next_node = i
                break
        mask ^= (1 << last_node)
        last_node = next_node

    tsp_route.append(0)  # Agregar el nodo de inicio
    tsp_route.reverse()  # Invertir la ruta para que esté en el orden correcto

    return tsp_route


# Función de búsqueda para el algoritmo de Ford-Fulkerson
def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

# Algoritmo de Ford-Fulkerson
def ford_fulkerson(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    return max_flow

# Función para encontrar la central más cercana
def closest_central(new_point, centrals):
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    closest = None
    min_distance = float('inf')
    for central in centrals:
        distance = euclidean_distance(new_point, central)
        if distance < min_distance:
            min_distance = distance
            closest = central
    return closest, min_distance
