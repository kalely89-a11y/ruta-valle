
# Ejercicio 10: Leer archivo CSV

import csv
import os

programas = {}

# Obtener la ruta del archivo
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta, "estudiantes.csv")

# Leer el archivo CSV
with open(ruta_csv, "r", encoding="utf-8-sig", newline="") as archivo:

    lector = csv.reader(archivo)

    # Ignorar filas vacías al principio
    filas = (fila for fila in lector if fila)

    # Leer encabezados
    encabezados = next(filas)

    print("Encabezados:", encabezados)

    # Recorrer estudiantes
    for fila in filas:

        nombre = fila[0].strip()
        programa = fila[1].strip()
        nota = float(fila[2].strip())

        if programa not in programas:
            programas[programa] = []

        programas[programa].append(nota)

# Crear archivo de promedios
ruta_salida = os.path.join(carpeta, "promedios.csv")

with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow(["programa", "promedio"])

    for programa, notas in programas.items():

        promedio = sum(notas) / len(notas)

        escritor.writerow([programa, f"{promedio:.2f}"])

print("Archivo promedios.csv creado correctamente")
