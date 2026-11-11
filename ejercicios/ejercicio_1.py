
# Recibir una nota y determinar si el estudiante aprobó o reprobó

nota = float(input("Ingrese la nota del estudiante (0 a 5): "))

if nota < 0 or nota > 5:
    print("La nota no es válida")
elif nota >= 3:
    print("Aprobó")
else:
    print("Reprobó")
