"""
Titulo: Actividad Integradora

Creado en: 02/10/2024
Actualizado en: 05/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripcion del codigo:
Este archivo implementa el algoritmo Z, que se usa para buscar patrones en las transmisiones. Crea un array Z que indica las longitudes de los prefijos más largos que coinciden con el comienzo de la cadena. Con esto, encuentra coincidencias entre los códigos maliciosos (mcodes) y las transmisiones, ayudando a detectar posibles infecciones de virus de manera rápida y eficiente.

"""

def calculate_z(s): 
    """
    Calcula el array Z para una cadena dada. El array Z indica, para cada 
    posición i, la longitud de la subcadena más larga que comienza en i y 
    coincide con un prefijo de la cadena s.

    Parámetros:
    s (str): La cadena para la cual se quiere calcular el array Z.

    Retorna:
    list: El array Z que contiene la longitud de las coincidencias prefijo para
    cada índice de la cadena.
    """

    Z = [0] * len(s)
    left, right, K = 0, 0, 0
    for i in range(1, len(s)):
        if i > right:
            left, right = i, i
            while right < len(s) and s[right] == s[right - left]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            K = i - left
            if Z[K] < right - i + 1:
                Z[i] = Z[K]
            else:
                left = i
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                Z[i] = right - left
                right -= 1
    return Z

def z_algorithm_search(text, pattern):
    """
    Realiza la búsqueda de un patrón en un texto utilizando el algoritmo Z.

    La función concatena el patrón y el texto con un separador especial ('$'),
    y luego calcula el array Z. Las posiciones donde el valor Z es igual a la 
    longitud del patrón son las posiciones de las coincidencias del patrón en el texto.

    Parámetros:
    text (str): El texto donde se desea buscar el patrón.
    pattern (str): El patrón que se busca dentro del texto.

    Retorna:
    list: Una lista de posiciones (0-based) donde el patrón coincide en el texto.
    """

    # Concatenamos el patrón, un separador especial, y el texto.
    concat = pattern + "$" + text
    Z = calculate_z(concat)

    result = []
    pattern_len = len(pattern)
    
    # Buscamos donde el valor Z es igual al tamaño del patrón
    for i in range(len(Z)):
        if Z[i] == pattern_len:
            result.append(i - pattern_len - 1)
    
    return result