
# Comprobar si una palabra se lee igual de izquierda a derecha y de derecha a izquierda.

palabra = input("Ingrese una palabra: ")

palabra = palabra.lower().replace(" ", "")

invertida = palabra[::-1]

if palabra == invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
