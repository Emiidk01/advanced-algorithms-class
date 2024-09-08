""" -----------------------------------------------------

Implementation of the "Branch and bound" technique for the Maze Challenge

Created On: 07/09/2024
Updated On: 07/09/2024

Authors:
    Angel Mauricio Ramirez Herrera - A01710158
    Cristian Chavez Guia - A0171680
    Emiliano Gomez Gonzalez - A01710711

Resources:
    https://es.wikipedia.org/wiki/Ramificaci%C3%B3n_y_poda

 -----------------------------------------------------
"""

import heapq

def es_factible(x, y, M, N, maze):
    """
    Checks if a position (x, y) is valid within the maze.

    Args:
        x (int): Row coordinate of the current position.
        y (int): Column coordinate of the current position.
        M (int): Number of rows in the maze.
        N (int): Number of columns in the maze.
        maze (list of list of int): Matrix representing the maze, 
                                    where 1 indicates a valid path and 0 an obstacle.

    Returns:
        bool: True if the position is valid and accessible (within bounds and on a valid path), False otherwise.
    """

    return 0 <= x < M and 0 <= y < N and maze[x][y] == 1

def G(x, y, M, N):
    """
    Calculates the heuristic estimate of the distance from a position (x, y) 
    to the goal at the bottom-right corner of the maze using the Manhattan distance.

    Args:
        x (int): Row coordinate of the current position.
        y (int): Column coordinate of the current position.
        M (int): Number of rows in the maze.
        N (int): Number of columns in the maze.

    Returns:
        int: The Manhattan distance from position (x, y) to the goal (M-1, N-1).
    """

    return abs(x - (M - 1)) + abs(y - (N - 1))

def resolver_laberinto(maze, M, N):
    """
    Solves the maze using a Branch and Bound algorithm with a priority queue.
    Finds the shortest path from the top-left corner (0, 0) to the bottom-right corner (M-1, N-1).

    Args:
        maze (list of list of int): Matrix representing the maze, 
                                    where 1 indicates a valid path and 0 an obstacle.
        M (int): Number of rows in the maze.
        N (int): Number of columns in the maze.

    Returns:
        list of list of int: A matrix of the same size as the maze, with 1s indicating the found path 
                             and 0s elsewhere. Returns None if no path is found.
    """
    
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    pq = [(G(0, 0, M, N), 0, 0, [(0, 0)])]
    visited = set()

    while pq:
        estimacion, x, y, path = heapq.heappop(pq)

        if (x, y) == (M - 1, N - 1):
            return marcar_ruta(maze, path, M, N)

        visited.add((x, y))

        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if es_factible(nx, ny, M, N, maze) and (nx, ny) not in visited:
                new_path = path + [(nx, ny)]
                heapq.heappush(pq, (G(nx, ny, M, N) + len(new_path), nx, ny, new_path))

    return None

def marcar_ruta(maze, path, M, N):
    """
    Marks the found path in a new matrix, maintaining the size of the original maze.

    Args:
        maze (list of list of int): Matrix representing the original maze.
        path (list of tuple): List of tuples with the coordinates (x, y) of the found path.
        M (int): Number of rows in the maze.
        N (int): Number of columns in the maze.

    Returns:
        list of list of int: A new matrix with 1s in the positions forming the path and 0s elsewhere.
    """
        
    maze_con_ruta = [[0 for _ in range(N)] for _ in range(M)]
    for x, y in path:
        maze_con_ruta[x][y] = 1
    return maze_con_ruta
