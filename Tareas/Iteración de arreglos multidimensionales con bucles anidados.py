# Crear una matriz 3D para almacenar datos de temperaturas
# Actividad sobre una matriz 3D que representa los datos de temperaturas
print('Hola bienvenidos')
print('¿Deseas conocer las temperaturas promedio de Quito, Guayaquil y Cuenca?')
nombre=input('Antes de iniciar ayudanos con tu nombre: ')
print(f"Un gusto conocerte {nombre}")
print("A continuación veamos las temperaturas promedios: ")
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 6},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 9}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 8},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": .26},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 10}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad = no_ciudad + 1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 1
        suma = 0
        for dia in semana:
            suma = suma + dia['temp']
        promedio = round(suma / len(semana), 1)
        suma_promedio += promedio
print(f'El promedio semana No. {no_semana} es: {promedio}')
promedio_ciudad = round(suma_promedio / len(ciudad), 1)
print(f'El promedio mensual es: {promedio_ciudad}')
print("Espero que te haya gustado, antes de terminar ¿Puedes decirnos qué tal te pareció?")
A=input('Puedes escibir si fue excelente, más o menos o pésimo: ')
print(f"Te parecio {A} gracias por tus comentarios")
