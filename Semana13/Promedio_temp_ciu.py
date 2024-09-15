temp = [
    [ #Cuenca
        [#Semana1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 23}
        ],
        [#Semana2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [ #Guayaquil
        [#Semana1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 21}
        ],
        [#Semana2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 26}
        ]
    ]
]
ciu= ["Cuenca","Guayaquil"]
for c_i,ciudad in enumerate(temp):
    for s_i, semana in enumerate(ciudad):
        sum_temp=sum([dia["temp"]for dia in semana])
        prom=sum_temp/len(semana)
        print(f"Promedio de temperaturas en {ciu[c_i]}, Semana {s_i + 1}: {prom:.2f} grados")


#SEMANA13

#FUNCION calcular promedio de temperatura por ciudad
def calcular_promedio_temperaturas(datos, nombres_ciudades):

    promedios = {}

    # Iterar sobre cada ciudad
    for c_i, ciudad in enumerate(datos):
        total_temp = 0
        total_dias = 0

        # Iterar sobre las semanas de cada ciudad
        for semana in ciudad:
            total_temp += sum([dia["temp"] for dia in semana])  # Sumar todas las temperaturas de la semana
            total_dias += len(semana)  # Contar los días en la semana

        # Calcular el promedio de CADA ciudad
        promedio_ciudad = total_temp / total_dias
        promedios[nombres_ciudades[c_i]] = promedio_ciudad

    return promedios
# Nombres de las ciudades
ciu = ["Cuenca", "Guayaquil"]

# Llamada a la función para calcular los promedios
promedios = calcular_promedio_temperaturas(temp, ciu)

# Mostrar los resultados
for ciudad, promedio in promedios.items():
    print(f"Promedio de temperatura en {ciudad}: {promedio:.2f} grados")