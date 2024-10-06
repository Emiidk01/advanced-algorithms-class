"""
Titulo: Actividad Integradora

Creado en: 02/10/2024
Actualizado en: 02/10/2024

Autores:
Angel Mauricio Ramirez Herrera - A01710158
Cristian Chavez Guia - A0171680
Emiliano Gomez Gonzalez - A01710711

Descripcion del codigo:
Funcion ma
"""

import z_algorithm
import os

def analizar_archivos(transmision1, transmision2, mcode1, mcode2, mcode3):
    # lista con los nombres de los archivos
    nom_archivos = [transmision1, transmision2, mcode1, mcode2, mcode3]
    contenido_archivos = []

    # leer el contenido de cada archivo, verificando si existen
    for nombre in nom_archivos:
        if not os.path.exists(nombre):
            print(f"Archivo {nombre} no encontrado")
            return  # Si algun archivo no se encuentra, termina la ejecucion
        with open(nombre, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            contenido_archivos.append(contenido)

    # asignar transmisiones y mcodes
    transmisiones = [contenido_archivos[0], contenido_archivos[1]]
    mcodes = [contenido_archivos[2], contenido_archivos[3], contenido_archivos[4]]

    for i, transmision in enumerate(transmisiones):
        print(f"\nArchivo transmission {i + 1}:\n{transmision}:")
    
    for i, mcode in enumerate(mcodes):
        print(f"\nArchivo mcode {i + 1}:\n{mcode}:")

    # iterar a traves de cada transmision y comparar con cada mcode
    for i, transmision in enumerate(transmisiones):
        print(f"\nArchivo transmission {i + 1}:")

        for j, mcode in enumerate(mcodes):
            # usar el algoritmo z para buscar el mcode en la transmision
            posiciones = z_algorithm.z_algorithm_search(transmision, mcode)

            # mostrar resultados segun el formato de salida
            if posiciones:
                # si se encuentra el patron muestra true y la primera posicion encontrada (indice basado en 0)
                print(f"\nmcode {j + 1}\n(true) Posicion inicial: {posiciones[0]}")
            else:
                print(f"\nmcode {j + 1}\n(false) Cadena no encontrada")

analizar_archivos('transmission01.txt', 'transmission12.txt', 'mcode01.txt', 'mcode02.txt', 'mcode03.txt')





            