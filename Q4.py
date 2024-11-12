def ordenar_pilha(pilha_original):
    pilha_ordenada = []

    while pilha_original:
        temp = pilha_original.pop()

        while pilha_ordenada and pilha_ordenada[-1] > temp:
            pilha_original.append(pilha_ordenada.pop())

        pilha_ordenada.append(temp)

    return pilha_ordenada

pilha = [5, 2, 8, 1, 9, 4]
print(ordenar_pilha(pilha.copy()))