#creacion de la matriz 3x3
matriz = [
    [1, 2, 3 ],
    [4, 5, 6 ],
    [7, 8, 9 ]
]
#funcion para buscar numero dentro de la matriz
def busca_numero(matriz,numero):
    for i in range(len(matriz)):#busco en la filas de la matriz
        for j in range(len(matriz[i])):#busco en las columnas de la matriz
            if matriz [i][j] == numero: #comparativa de los valores de filas y columnas de la matriz con el numero
                return (i,j) #devuelve fila y columna del valor encontrado
    return None #sin datos si el numero no se encontro
valor_a_buscar = 3 #defino el numero a buscar
posicion = busca_numero(matriz, valor_a_buscar) #busco el valor en la matriz


# if para mostrar el resultado en pantalla
if posicion:
    #resultado positivo si el numero se encontro, mostrando posicion en filas y columnas
    print("el numero", valor_a_buscar,"se encontro en la posicion fila: ", posicion,"columna",posicion )
else:
    #resultado negativo si el numero a buscar no se encuentra en la matriz

    print("el numero", valor_a_buscar, "no se encontro en la matriz")
    
        