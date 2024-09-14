def bubble_sort(row):
    n=len(row)
    for i in range(n):#bucle que controla "n" veces antes de ordenar de manera ascendente
        for j in range(n-i-1):
            if row [j] > row [j+1]:#comparacion si row j es mayor al seguiente dato, que es row j+1
                row[j], row[j + 1] = row[j + 1], row[j]#paso burbuja, donde el elemento mas grande se mueve al final de la lista,
    return row#devuelve la fila ordenada despues del bucle i y j

#creacion de la matriz inicial
def mostrar_matriz(matriz): #funcion para crear mi matriz
    for fila in matriz: #bucle for que itera sobre cada fila de la matriz
        print(fila)#imprimo mi matriz sin ordenar
matriz = [
    [8,4,7],
    [2,1,3],
    [5,9,6]
]
print("Matriz sin ordenar")
mostrar_matriz(matriz)

#imprimir matriz ordenada
fila_a_ordenar=0# fila que deseo ordenar de manera ascendente
matriz[fila_a_ordenar]=bubble_sort(matriz[fila_a_ordenar])#llamo a la funcion burbuja para ordenar la fila designada, luego regreso la fila ordenada a su posicion inicial en la matriz sin ordenar

print("matriz con la fila", fila_a_ordenar, "ordenada")
mostrar_matriz(matriz)