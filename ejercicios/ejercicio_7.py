
#  Eliminar los números repetidos de una lista de dos maneras diferentes

numeros = [1, 2, 2, 3, 4, 4, 5]

sin_duplicados = []

for numero in numeros:

    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print("Lista sin duplicados:", sin_duplicados)
