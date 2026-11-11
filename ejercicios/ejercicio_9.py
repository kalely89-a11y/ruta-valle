
#  Comparar los pagos registrados con los movimientos del banco.

pagos = [
    {"codigo": "P01", "valor": 100000},
    {"codigo": "P02", "valor": 200000},
    {"codigo": "P03", "valor": 150000}
]

banco = [
    {"codigo": "P01", "valor": 100000},
    {"codigo": "P02", "valor": 180000}
]

# Crear un diccionario con los movimientos bancarios
movimientos = {}

for movimiento in banco:
    movimientos[movimiento["codigo"]] = movimiento["valor"]

# Comparar los pagos
for pago in pagos:

    codigo = pago["codigo"]
    valor = pago["valor"]

    if codigo not in movimientos:
        print(codigo, "- No aparece en el banco")

    elif movimientos[codigo] == valor:
        print(codigo, "- Aparece con el mismo valor")

    else:
        print(codigo, "- Aparece con otro valor")
