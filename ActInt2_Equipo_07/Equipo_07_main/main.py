"""
Titulo: Actividad Integradora 2

Creado en: 9/11/2024
Actualizado en: 10/11/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711
"""

# Imports necesarios
import sys
import itertools
import math
import heapq
from ActInt2_Equipo_07.Equipo_07_main.utils import kruskal_mst, tsp_dp, ford_fulkerson, closest_central

def load_input(file_path):
    """Carga los datos de entrada desde un archivo.

    Parámetros:
        file_path (str): La ruta al archivo de entrada.

    Devuelve:
        tuple: Una tupla que contiene el número de colonias (int), la matriz de adyacencia con distancias (lista de listas),
               la matriz de capacidades máximas de flujo (lista de listas), una lista de tuplas con las coordenadas de cada
               central (lista de tuplas), y las coordenadas de la nueva central (tupla).

    Complejidad:
        O(N^2) - Debido a la lectura de dos matrices de tamaño N x N desde el archivo.
    """
    with open(file_path, 'r') as file:
        N = int(file.readline().strip())
        
        # Leer matriz de distancias en kilómetros
        kms_matrix = []
        for _ in range(N):
            row = list(map(int, file.readline().strip().split()))
            kms_matrix.append(row)
        
        # Leer matriz de capacidades de flujo
        capacities = []
        for _ in range(N):
            row = list(map(int, file.readline().strip().split()))
            capacities.append(row)
        
        # Leer coordenadas de las centrales
        central_coords = []
        for _ in range(N):
            x, y = map(int, file.readline().strip().split(','))
            central_coords.append((x, y))
        
        # Leer la coordenada de la nueva central
        new_contract_coord = tuple(map(int, file.readline().strip().split(',')))
    
    return N, kms_matrix, capacities, central_coords, new_contract_coord

def main(file_path):
    """Función principal para ejecutar las tareas especificadas en el enunciado del problema.

    Parámetros:
        file_path (str): La ruta al archivo de entrada.
    """

    N, kms_matrix, capacities, central_coords, new_contract_coord = load_input(file_path)

    # 1. Calcular el árbol de expansión mínima para el cableado de fibra óptica
    mst_edges, mst_weight = kruskal_mst(kms_matrix)
    print("Forma óptima de cablear con fibra óptica (usando MST):")
    for u, v, weight in mst_edges:
        print(f"{chr(65 + u)} -- {chr(65 + v)}: {weight} km")

    # 2. Ruta más corta para el repartidor (Resolviendo el TSP)
    tsp_route, min_cost = tsp_dp(kms_matrix)
    print("\nRuta más corta para visita de correspondencia:")
    print(" --> ".join(chr(65 + i) for i in tsp_route))
    print(f"Distancia total: {min_cost} km")

    # 3. Cálculo del flujo máximo de información
    source, sink = 0, N - 1  # Definir los nodos de origen y destino
    max_flow = ford_fulkerson(capacities, source, sink)
    print("\nFlujo máximo de información:")
    print(f"Flujo máximo entre nodo {chr(65 + source)} y nodo {chr(65 + sink)}: {max_flow}")

    # 4. Central más cercana a la nueva central
    closest, closest_distance = closest_central(new_contract_coord, central_coords)
    print("\nCentral más cercana:")
    print(f"Central en coordenadas {closest} con distancia: {closest_distance:.2f} km")

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    main(file_path)