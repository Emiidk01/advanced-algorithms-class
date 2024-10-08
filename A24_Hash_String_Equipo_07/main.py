"""
Titulo: Implementing Hash String

Creado en: 28/09/2024
Actualizado en: 28/09/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Code Description:
Este programa recibe un archivo de texto y un valor entero n, donde n debe ser un multiplo de 4
y estar en el rango de 16 a 64. El objetivo es crear una tabla con n columnas y llenar cada columna
con los caracteres del archivo. Luego, se calcula un arreglo a que contiene el valor de cada columna
ajustado por módulo 256 y, finalmente, se genera una cadena de salida en formato hexadecimal.
"""

"""
INSTRUCCIONES:

Escribe un programa que reciba el nombre de un archivo de texto (datos.txt), seguido de un entero n, donde n es
un entero múltiplo de 4 y (16 <= n <=64).

La salida es una cadena de longitud n/4 que es una representación hexadecimal que corresponde al hasheo del archivo
de texto de entrada de acuerdo con las siguientes reglas:

- El entero n determina el número de columnas que contendrá una tabla donde se irán acomodando los caracteres
del archivo de texto (incluyendo saltos de líneas) en los renglones que sean necesarios.

- Si el número de caracteres en el archivo de entrada no es múltiplo de n, el último renglón se "rellena" con el valor de n.

- En un arreglo a de longitud n se calcula a[i] = (la suma de los ASCII de cada char en la columna) % 256.

- La salida se genera concatenando la representación hexadecimal (mayúsculas) a dos dígitos de cada posición en el arreglo.

- La longitud de la cadena de salida será de n/4.

- Muestra la tabla generada, el arreglo a, y la cadena de salida.

"""

def procesar_archivo(nombre_archivo, n, caso_numero):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    print(f"\n{'='*10} Caso {caso_numero} (n = {n}) {'='*10}")

    # construccion de la tabla
    filas = len(contenido) // n + (1 if len(contenido) % n != 0 else 0)  # calcula cuantas filas serán necesarias
    tabla = [[''] * n for _ in range(filas)]  # tabla inicial vacia de tamaño filas x n

    # rellenar la tabla con los caracteres del archivo
    indice = 0
    for i in range(filas):
        for j in range(n):
            if indice < len(contenido):
                tabla[i][j] = contenido[indice]
                indice += 1
            else:
                tabla[i][j] = chr(n)  # rellena con el valor ASCII del numero n si no hay mas caracteres

    # mostrar la tabla generada
    print("\nTabla generada:")
    for fila in tabla:
        print("".join(fila))

    # calcular el arreglo a
    a = [0] * n
    for j in range(n):
        suma_columna = 0
        for i in range(filas):
            suma_columna += ord(tabla[i][j])  # suma los valores ASCII de cada columna
        a[j] = suma_columna % 256

    print("\nArreglo 'a':", a)

    # generar la cadena hexadecimal en bloques de 4 columnas
    salida_hex = []
    for i in range(0, n, 4):
        # concatenar los valores hexadecimales de 4 columnas en un solo bloque
        bloque = ''.join(f"{a[i + j]:02X}" for j in range(4))
        salida_hex.append(bloque)

    # mostrar la cadena de salida en bloques separados
    cadena_salida = " ".join(salida_hex)
    print("\nCadena de salida (en bloques de 4 columnas):", cadena_salida)

    return cadena_salida


# casos de prueba con diferentes valores de n
archivo1 = "caso1.txt"
archivo2 = "quijote.txt"
archivo3 = "littleprince.txt"
archivo4 = "frankenstein.txt"

print("\n\n--- Ejecucion de Casos de Prueba ---")

# Caso 1: n = 16
procesar_archivo(archivo1, 16, caso_numero=1)

# Caso 2: n = 32
procesar_archivo(archivo2, 32, caso_numero=2)

# Caso 3: n = 48
procesar_archivo(archivo3, 48, caso_numero=3)

# Caso 4: n = 64
procesar_archivo(archivo4, 64, caso_numero=4)



        




