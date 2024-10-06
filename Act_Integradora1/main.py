"""
Titulo: Actividad Integradora

Creado en: 02/10/2024
Actualizado en: 02/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripcion del codigo:
"""

import z_algorithm
import manacher
import longest_substr
import os

def analizar_archivos(transmision1, transmision2, mcode1, mcode2, mcode3):
    # lista con los nombres de los archivos
    nom_archivos = [transmision1, transmision2, mcode1, mcode2, mcode3]
    contenido_archivos = []

    # leer el contenido de cada archivo, verificando si existen
    for nombre in nom_archivos:
        if not os.path.exists(nombre):
            print(f"Archivo {nombre} no encontrado")
            return  # Si algún archivo no se encuentra, termina la ejecución
        with open(nombre, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            contenido_archivos.append(contenido)

    # asignar transmisiones y mcodes
    transmisiones = [contenido_archivos[0], contenido_archivos[1]]
    mcodes = [contenido_archivos[2], contenido_archivos[3], contenido_archivos[4]]

    virus_detectado = False  # Variable para controlar si se detecta un virus

    for i, transmision in enumerate(transmisiones):
        print(f"\nArchivo transmission {i + 1}:")

        # Almacenar posiciones de mcodes encontrados
        mcodes_encontrados = []

        for j, mcode in enumerate(mcodes):
            # usar el algoritmo z para buscar el mcode en la transmisión
            posiciones = z_algorithm.z_algorithm_search(transmision, mcode)

            # mostrar resultados según el formato de salida
            if posiciones:
                print(f"\nmcode {j + 1}\n(true) Posición inicial: {posiciones[0]}")
                mcodes_encontrados.append(mcode)
            else:
                print(f"\nmcode {j + 1}\n(false) Cadena no encontrada")

        # Verificar palíndromo solo si se encontró algún mcode
        if mcodes_encontrados:
            start, end = manacher.manacher(transmision)
            if start is not None and end is not None:
                print(f"\nPalíndromo más largo en transmission {i + 1} empieza en {start} y termina en {end}")
                
                # Verificar si todos los mcodes están contenidos en el palíndromo
                palindromo = transmision[start:end + 1]
                todos_encontrados = all(z_algorithm.z_algorithm_search(palindromo, mcode) for mcode in mcodes_encontrados)

                if todos_encontrados:
                    print("Todos los mcodes están contenidos dentro del palíndromo.")
                    virus_detectado = True

                # Invertir la transmisión y buscar nuevamente mcodes
                transmision_invertida = transmision[::-1]
                for mcode in mcodes:
                    posiciones = z_algorithm.z_algorithm_search(transmision_invertida, mcode)
                    if posiciones:
                        print(f"\nmcode {mcode} encontrado en la transmisión invertida.")
                        mcodes_encontrados.append(mcode)
                        virus_detectado = True
        
    # Verificar coincidencias entre las dos transmisiones
    start, end = longest_substr.longest_common_substring(transmisiones[0], transmisiones[1])
    if start is not None and end is not None:
        print(f"\nSubstring más largo común entre transmission 1 y 2 empieza en {start} y termina en {end}")
        if end - start + 1 > 2:  # Considera un substring común de longitud mínima 3 como indicio de virus
            print("Alta similitud entre las transmisiones. Posible virus detectado.")
            virus_detectado = True

    # Resultado final
    if virus_detectado:
        print("\nSe ha detectado un posible virus en las transmisiones.")
    else:
        print("\nNo se ha detectado ningún virus en las transmisiones.")

analizar_archivos('transmission01.txt', 'transmission12.txt', 'mcode01.txt', 'mcode02.txt', 'mcode03.txt')