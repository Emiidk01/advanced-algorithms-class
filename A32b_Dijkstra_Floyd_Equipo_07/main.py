"""
Titulo: Implementación de "Dijkstra and Floyd"

Creado en: 20/10/2024
Actualizado en: 20/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripción del código:

En este código se implementaron dos algoritmos fundamentales en la teoría de grafos:
Dijkstra y Floyd-Warshall, ambos usados para calcular rutas más cortas en un
grafo representado como una matriz de adyacencia. El algoritmo de Dijkstra se
enfoca en encontrar la distancia mínima desde un nodo de origen específico a
todos los demás nodos, empleando una cola de prioridad (heapq) para optimizar
el proceso de selección del nodo con la distancia más corta en cada paso.
Por otro lado, el algoritmo de Floyd-Warshall es una solución para calcular las
distancias mínimas entre todos los pares de nodos, probando si la ruta que pasa por
nodos intermedios ofrece un camino más corto. Ambos algoritmos
imprimen los resultados: Dijkstra mostrando las distancias desde un nodo
origen a los demás, y Floyd-Warshall desplegando una matriz completa de
distancias mínimas entre todos los pares de nodos.


El programa también contiene 4 casos de prueba que demuestran el funcionamiento del algoritmo.
"""

import test_cases

test_cases.start()