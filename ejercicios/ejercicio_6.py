

#Contar cuántas veces aparece cada palabra en un texto

texto = "Hola mundo hola software mundo hola"

texto = texto.lower()

palabras = texto.split()

contador = {}

for palabra in palabras:

    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

for palabra, cantidad in contador.items():
    print(palabra + ":", cantidad)
