import utils as u

def main():
    # Definir las matrices de distancias (representadas como matrices de adyacencia)
    adj_matrix1 = [
        [0, 16, 45, 32],
        [16, 0, 18, 21],
        [45, 18, 0, 7],
        [32, 21, 7, 0]
    ]
    adj_matrix2 = [
        [0, 48, 12, 18],
        [52, 0, 42, 32],
        [18, 46, 0, 56],
        [24, 36, 52, 0]
    ]

    # Centrales y nuevo punto
    centrals = [(200, 500), (300, 100), (450, 150), (520, 480)]
    new_point = (325, 200)

    # 1. Árbol de Expansión Mínima (Kruskal)
    mst_edges, mst_weight = u.kruskal_mst(adj_matrix1)
    print("Árbol de Expansión Mínima (Kruskal):")
    print("Aristas:", mst_edges)
    print("Peso total:", mst_weight)
    print()

    # 2. Problema del Viajante de Comercio (TSP)
    tsp_distance = u.tsp_dp(adj_matrix2)
    print("Problema del Viajante de Comercio (TSP):")
    print("Distancia mínima:", tsp_distance)
    print()

    # 3. Flujo máximo (Ford-Fulkerson)
    capacity = [
        [0, 16, 45, 32],
        [16, 0, 18, 21],
        [45, 18, 0, 7],
        [32, 21, 7, 0]
    ]
    max_flow = u.ford_fulkerson(capacity, 0, 3)
    print("Flujo máximo (Ford-Fulkerson):")
    print("Flujo máximo:", max_flow)
    print()

    # 4. Central más cercana
    closest, distance = u.closest_central(new_point, centrals)
    print("Central más cercana:")
    print("Central:", closest)
    print("Distancia:", distance)

if __name__ == "__main__":
    main()
