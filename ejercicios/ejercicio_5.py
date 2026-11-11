
# Organizar los estudiantes según el programa académico al que pertenecen.

estudiantes = [
    {"nombre": "Ana", "programa": "Software", "semestre": 2},
    {"nombre": "Pedro", "programa": "Diseño", "semestre": 3},
    {"nombre": "Luis", "programa": "Software", "semestre": 1},
    {"nombre": "María", "programa": "Diseño", "semestre": 4}
]

grupos = {}

for estudiante in estudiantes:

    programa = estudiante["programa"]
    nombre = estudiante["nombre"]

    if programa not in grupos:
        grupos[programa] = []

    grupos[programa].append(nombre)

for programa, nombres in grupos.items():

    print(programa + ":")

    for nombre in nombres:
        print("-", nombre)
