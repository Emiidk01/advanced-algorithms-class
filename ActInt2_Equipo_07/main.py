import sys
import itertools
import math
import heapq

# Matriz de distancias en kilómetros
kms_matrix = [
    [0, 16, 45, 32],
    [16, 0, 18, 21],
    [45, 18, 0, 7],
    [32, 21, 7, 0]
]

def dijkstra_from_matrix(kms_matrix, start_node):
    # Inicializamos el número de nodos
    n = len(kms_matrix)
    
    # Inicializar distancias (todas a infinito, excepto la del nodo de inicio)
    distances = [float('inf')] * n
    distances[start_node] = 0
    
    # Cola de prioridad para procesar los nodos de acuerdo con la distancia más corta
    priority_queue = [(0, start_node)]  # (distancia, nodo)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si la distancia actual es mayor que la ya registrada, continuar al siguiente
        if current_distance > distances[current_node]:
            continue
        
        # Recorremos los nodos vecinos de la matriz de distancias
        for neighbor in range(n):
            if neighbor != current_node:  # Evitamos volver al nodo actual
                distance = current_distance + kms_matrix[current_node][neighbor]
                
                # Si encontramos una ruta más corta a un nodo vecino, actualizamos la distancia
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Nodo de inicio (por ejemplo, el nodo 0, correspondiente a la primera fila/columna de la matriz)
start_node = 0

# Llamamos a la función para calcular las distancias más cortas desde el nodo de inicio
shortest_paths = dijkstra_from_matrix(kms_matrix, start_node)

# Mostrar los resultados
print(f"Las distancias más cortas desde el nodo {start_node} son:")
for node, distance in enumerate(shortest_paths):
    print(f"Nodo {node}: {distance} km")

# Nodo de inicio (por ejemplo, el nodo 0, correspondiente a la primera fila/columna de la matriz)
start_node = 1

# Llamamos a la función para calcular las distancias más cortas desde el nodo de inicio
shortest_paths = dijkstra_from_matrix(kms_matrix, start_node)

# Mostrar los resultados
print(f"Las distancias más cortas desde el nodo {start_node} son:")
for node, distance in enumerate(shortest_paths):
    print(f"Nodo {node}: {distance} km")

# Nodo de inicio (por ejemplo, el nodo 0, correspondiente a la primera fila/columna de la matriz)
start_node = 2

# Llamamos a la función para calcular las distancias más cortas desde el nodo de inicio
shortest_paths = dijkstra_from_matrix(kms_matrix, start_node)

# Mostrar los resultados
print(f"Las distancias más cortas desde el nodo {start_node} son:")
for node, distance in enumerate(shortest_paths):
    print(f"Nodo {node}: {distance} km")

# Nodo de inicio (por ejemplo, el nodo 0, correspondiente a la primera fila/columna de la matriz)
start_node = 3

# Llamamos a la función para calcular las distancias más cortas desde el nodo de inicio
shortest_paths = dijkstra_from_matrix(kms_matrix, start_node)

# Mostrar los resultados
print(f"Las distancias más cortas desde el nodo {start_node} son:")
for node, distance in enumerate(shortest_paths):
    print(f"Nodo {node}: {distance} km")

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
