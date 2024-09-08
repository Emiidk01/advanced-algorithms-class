"""
-----------------------------------------------------

Implementation of the "Branch and bound" technique for the Maze Challenge

Created On: 07/09/2024
Updated On: 07/09/2024

Authors:
    Angel Mauricio Ramirez Herrera - A01710158
    Cristian Chavez Guia - A0171680
    Emiliano Gomez Gonzalez - A01710711

-----------------------------------------------------
"""

from utils.inputs import laberintos
from poda import resolver_laberinto

for index, laberinto in enumerate(laberintos):
    M = laberinto["M"]
    N = laberinto["N"]
    maze = laberinto["maze"]
    solution = resolver_laberinto(maze, M, N)
    print(f"Laberinto {index + 1} - Ruta encontrada:" if solution else f"Laberinto {index + 1} - No hay ruta disponible")
    if solution:
        for row in solution:
            print(' '.join(map(str, row)))
    else:
        print("No se encontró una ruta.")