def count_pedidos_impares(pilha_pedidos):
    contador_impares = 0
    pilha_auxiliar = []  

    while pilha_pedidos:
        pedido = pilha_pedidos.pop()
        if pedido % 2 == 0:  
            contador_impares += 1
        pilha_auxiliar.append(pedido)

    while pilha_auxiliar:
        pilha_pedidos.append(pilha_auxiliar.pop())

    return contador_impares

pedidos = [10, 3, 15, 22, 7, 12, 19]
print(count_pedidos_impares(pedidos))