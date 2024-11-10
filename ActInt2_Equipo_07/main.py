import sys
import itertools
import math

# Matriz de distancias en kilómetros
kms_matrix = [
    [0, 16, 45, 32],
    [16, 0, 18, 21],
    [45, 18, 0, 7],
    [32, 21, 7, 0]
]

def prim_mst(matrix):
    num_nodes = len(matrix)
    selected_nodes = [False] * num_nodes
    selected_nodes[0] = True
    mst_edges = []

    for _ in range(num_nodes - 1):
        min_edge = (None, None, sys.maxsize)  # (start, end, weight)
        
        for i in range(num_nodes):
            if selected_nodes[i]:
                for j in range(num_nodes):
                    if not selected_nodes[j] and matrix[i][j] != 0 and matrix[i][j] < min_edge[2]:
                        min_edge = (i, j, matrix[i][j])

        mst_edges.append(min_edge)
        selected_nodes[min_edge[1]] = True

    return mst_edges

mst = prim_mst(kms_matrix)
print("Árbol de Expansión Mínima (Cableado Óptimo):")
for edge in mst:
    print(f"Km de colonia {chr(65 + edge[0])} a colonia {chr(65 + edge[1])}: {edge[2]}")

# Generamos todas las permutaciones posibles de nodos (colonias) excluyendo el nodo inicial
colonies = [0, 1, 2, 3]
shortest_path = None
min_distance = sys.maxsize

for perm in itertools.permutations(colonies[1:]):
    path = [0] + list(perm) + [0]
    distance = sum(kms_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    if distance < min_distance:
        min_distance = distance
        shortest_path = path

print("\nCamino más corto:")
print(" --> ".join(chr(65 + i) for i in shortest_path))
print(f"Distancia total: {min_distance} km")

# Matriz de capacidades entre colonias
capacities = [
    [0, 48, 12, 18],
    [52, 0, 42, 32],
    [18, 46, 0, 56],
    [24, 36, 52, 0]
]

def dfs(capacity_matrix, source, sink, visited, path):
    if source == sink:
        return path
    visited[source] = True

    for i, capacity in enumerate(capacity_matrix[source]):
        if not visited[i] and capacity > 0:  # there's capacity left and node is unvisited
            result = dfs(capacity_matrix, i, sink, visited, path + [(source, i)])
            if result is not None:
                return result
    return None

def ford_fulkerson(capacity_matrix, source, sink):
    max_flow = 0
    residual_matrix = [row[:] for row in capacity_matrix]

    while True:
        visited = [False] * len(capacity_matrix)
        path = dfs(residual_matrix, source, sink, visited, [])

        if path is None:
            break  # no more augmenting paths

        # Find the maximum flow we can send along this path
        path_flow = min(residual_matrix[u][v] for u, v in path)

        # Update residual capacities of the edges and reverse edges along the path
        for u, v in path:
            residual_matrix[u][v] -= path_flow
            residual_matrix[v][u] += path_flow

        max_flow += path_flow

    return max_flow

source, sink = 0, 3  # Nodo inicial (0) a nodo final (3)
max_flow = ford_fulkerson(capacities, source, sink)
print("\nFlujo máximo:")
print(f"Flujo máximo de información: {max_flow}")

# Coordenadas de las centrales
centrals_coords = [
    (200, 500),
    (300, 100),
    (450, 150),
    (520, 480)
]

# Coordenada de la nueva contratación
new_contract_coord = (325, 200)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

closest_distance = sys.maxsize
closest_central = None
for i, coord in enumerate(centrals_coords):
    dist = euclidean_distance(new_contract_coord, coord)
    if dist < closest_distance:
        closest_distance = dist
        closest_central = i

print("\nDistancia mínima:")
print(f"Central más cercana: {closest_central + 1}, Distancia: {closest_distance:.2f} km")
