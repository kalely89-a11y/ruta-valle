
#  Imprimir los números del 1 al 100 aplicando las reglas de múltiplos

for numero in range(1, 101):

    if numero % 3 == 0 and numero % 5 == 0:
        print("ValleSoftware")

    elif numero % 3 == 0:
        print("Valle")

    elif numero % 5 == 0:
        print("Software")

    else:
        print(numero)
