def contar_livros_impares(fila):
    contador_impares = 0

    for livro_id in fila:
        if livro_id % 2 != 0: 
            contador_impares += 1
    return contador_impares

fila_livros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_livros_impares(fila_livros))