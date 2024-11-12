def ordenar_fila(fila):
    n = len(fila)

    if n <= 1:
        return 

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if fila[j] < fila[min_index]:
                min_index = j

        fila[i], fila[min_index] = fila[min_index], fila[i]

fila = [3, 1, 4, 1, 5, 9, 2, 6]
ordenar_fila(fila)
print(fila)