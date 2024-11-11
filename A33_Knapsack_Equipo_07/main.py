"""
Titulo: Implementación de "Knapsack"

Creado en: 02/11/2024
Actualizado en: 02/11/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripción del código:

El Knapsack Problem (Problema de la Mochila) es un clásico problema
de optimización en teoría de la computación y matemáticas combinatorias.
Se plantea de la siguiente manera: dado un conjunto de elementos,
cada uno con un peso y un valor, se debe determinar la combinación
de elementos que se pueden incluir en una mochila de capacidad limitada
de tal forma que el valor total de los elementos incluidos sea el máximo
posible, sin exceder la capacidad máxima de la mochila

El programa también contiene 4 casos de prueba que
demuestran el funcionamiento del algoritmo.
"""

from itertools import combinations

items = [
    {"weight": 1, "value": 4},
    {"weight": 2, "value": 5},
    {"weight": 3, "value": 1},
]

capacity = 4


# O(2^n)
def knapsack_brute_force(items, capacity):
    """
    Solves the 0/1 knapsack problem using a brute-force approach.

    This function explores all possible combinations of items and selects the 
    combination that provides the maximum value without exceeding the capacity.

    Args:
        items (list): A list of dictionaries where each dictionary represents 
                      an item with 'weight' and 'value' keys.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        tuple: A tuple containing:
            - best_value (int): The maximum value achievable.
            - best_combination (list): The combination of items that yields 
                                       the best value.
            - used_capacity (int): The total weight of the chosen combination.
    """
    n = len(items)
    best_value = 0
    best_combination = None
    used_capacity = None

    for r in range(n + 1):
        for combination in combinations(items, r):
            total_weight = sum(item['weight'] for item in combination)
            total_value = sum(item['value'] for item in combination)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combination
                used_capacity = total_weight

    return best_value, best_combination, used_capacity


# O(n log n)
def knapsack_greedy(items, capacity):
    """
    Solves the 0/1 knapsack problem using a greedy approach.

    This function sorts items based on their value-to-weight ratio and picks 
    them in descending order until the capacity is reached or all items are used.

    Args:
        items (list): A list of dictionaries where each dictionary represents 
                      an item with 'weight' and 'value' keys.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        tuple: A tuple containing:
            - total_value (int): The total value of the selected items.
            - chosen_items (list): The list of chosen items.
            - total_weight (int): The total weight of the chosen items.
    """
    items_sorted = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)
    total_value = 0
    total_weight = 0
    chosen_items = []

    for item in items_sorted:
        if total_weight + item['weight'] <= capacity:
            chosen_items.append(item)
            total_weight += item['weight']
            total_value += item['value']

    return total_value, chosen_items, total_weight


# O(nW)
def knapsack_dynamic(items, capacity):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    This function constructs a 2D table to find the maximum value that can be 
    achieved with a given capacity and set of items. It reconstructs the list 
    of chosen items based on the DP table.

    Args:
        items (list): A list of dictionaries where each dictionary represents 
                      an item with 'weight' and 'value' keys.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        tuple: A tuple containing:
            - total_value (int): The maximum value achievable.
            - total_weight (int): The total weight of the chosen items.
            - chosen_items (list): The list of items included in the knapsack.
            - dp (list): The DP table used for solving the problem.
    """
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1]['weight'] <= w:
                dp[i][w] = max(items[i - 1]['value'] +
                               dp[i - 1][w - items[i - 1]['weight']],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    chosen_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(items[i - 1])
            w -= items[i - 1]['weight']

    total_weight = sum(item['weight'] for item in chosen_items)
    total_value = dp[n][capacity]
    return total_value, total_weight, chosen_items, dp


print("Beneficio optimo: ", knapsack_dynamic(items, capacity)[1])
print("Matriz generada: ", knapsack_dynamic(items, capacity)[-1])
