"""
Creado en: 20/10/2024
Actualizado en: 20/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711
Función start

Descripción: Ejecuta una serie de casos de prueba donde se aplican los algoritmos de Dijkstra y Floyd-Warshall 
para encontrar las distancias más cortas entre todos los pares de nodos en un grafo dirigido. 
Los casos de prueba están definidos como matrices de adyacencia donde los pesos de los arcos 
entre los nodos están representados por números enteros, y -1 indica la ausencia de una arista.

Casos de prueba: Cada caso de prueba es un diccionario con las siguientes claves:
- "n" (int): Número de nodos en el grafo.
- "m" (List[List[int]]): Matriz de adyacencia que representa los pesos de los arcos. Si no hay arco, el valor es -1.
    
Función:
- Llama a la función utils.dijkstra() para cada nodo en el grafo, mostrando las distancias mínimas desde el nodo de inicio.
- Llama a la función utils.floyd_warshall() para calcular las distancias mínimas entre todos los nodos del grafo.

Retorno:
None. La función imprime las distancias calculadas para cada caso de prueba utilizando los algoritmos de Dijkstra y Floyd-Warshall.

Dependencias:
Esta función depende de las funciones utils.dijkstra() y utils.floyd_warshall() para realizar los cálculos.
"""

import utils

# Definimos los casos de prueba en el formato adecuado
test_cases = [
    {
        "n": 4,
        "m": [[0, 2, -1, 3],
              [-1, 0, 1, 5],
              [2, 3, 0, -1],
              [3, -1, 4, 0]]
    },
    {
        "n": 3,
        "m": [[0, 2, -1],
              [-1, 0, 1],
              [2, 3, 0]]
    },
    {
        "n": 2,
        "m": [[0, 2],
              [7, 0]]
    },
    {
        "n": 5,
        "m": [[0, 2, 4, 2, 6],
              [-1, 0, 10, 1, -1],
              [6, 4, 0, 2, 1],
              [-1, -1, 2, 0, 1],
              [2, 5, 6, 7, 0]]
    }
]

def start():
    # Ejecutamos cada caso de prueba
    for test in test_cases:
        n = test["n"]
        graph = test["m"]

        # Dijkstra para cada nodo
        print("Dijkstra:")
        for i in range(n):
            utils.dijkstra(i, graph)

        # Floyd-Warshall
        utils.floyd_warshall(graph)