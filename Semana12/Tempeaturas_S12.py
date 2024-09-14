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