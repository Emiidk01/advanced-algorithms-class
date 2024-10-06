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

def manacher(s):
    # Preprocesar la cadena para manejar palíndromos de longitud par
    T = '#'.join(f'^{s}$')  # Se agregan caracteres especiales al inicio y al final
    n = len(T)
    P = [0] * n  # Array para guardar las longitudes de los palíndromos
    C = R = 0  # Centro y límite derecho del palíndromo

    for i in range(1, n - 1):
        mirr = 2 * C - i  # La posición espejo respecto al centro

        if R > i:
            P[i] = min(R - i, P[mirr])  # Evitar ir más allá del límite derecho

        # Intentar expandir el palíndromo alrededor de i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Actualizar el centro y el límite derecho si se expande más allá
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Encontrar el índice del palíndromo más largo
    max_length = max(P)
    center_index = P.index(max_length)

    # Convertir la longitud y los índices a la cadena original
    start = (center_index - max_length) // 2  # Iniciar índice en cadena original
    end = start + max_length - 1  # Terminar índice en cadena original

    return start + 1, end + 1  # Convertir a 1-based index
