"""
Titulo: Actividad Integradora

Creado en: 02/10/2024
Actualizado en: 05/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripcion del codigo:
"""

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Crear una matriz para almacenar las longitudes de los substrings comunes
    LCSuff = [[0] * (n + 1) for _ in range(m + 1)]
    
    longest_length = 0
    ending_index_s1 = 0  # Índice de finalización del substring más largo en s1

    # Llenar la matriz LCSuff
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > longest_length:
                    longest_length = LCSuff[i][j]
                    ending_index_s1 = i  # Actualizar índice de finalización en s1
            else:
                LCSuff[i][j] = 0  # Reiniciar si no hay coincidencia

    # Verificar si se encontró un substring
    if longest_length == 0:
        return None, None  # Si no hay coincidencias, devolver None

    # Devolver la posición inicial y final (1-based index)
    start = ending_index_s1 - longest_length + 1
    end = ending_index_s1  # El índice final es el índice de finalización

    return start, end  # Posiciones 1-based
