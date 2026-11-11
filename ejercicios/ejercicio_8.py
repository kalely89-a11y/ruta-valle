
# Verificar que un pago tenga un valor válido, una fecha correcta y un código no vacío.

from datetime import datetime

pago = {
    "valor": -500,
    "fecha": "2026/11/10",
    "codigo": ""
}

errores = []

# Validar el valor
if type(pago["valor"]) != int or pago["valor"] <= 0:
    errores.append("El valor debe ser un entero positivo")

# Validar la fecha
try:
    fecha = datetime.strptime(pago["fecha"], "%Y-%m-%d")
except ValueError:
    errores.append("La fecha no tiene el formato correcto")

# Validar el código
if not pago["codigo"].strip():
    errores.append("El código está vacío")

# Mostrar resultados
if errores:
    print(errores)
else:
    print("El pago es válido")
