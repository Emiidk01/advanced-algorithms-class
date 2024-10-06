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

def calculate_z(s):
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