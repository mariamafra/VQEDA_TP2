def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_set(lista):
    checados = set()
    duplicados = set()
    for item in lista:
        if item in checados:
            duplicados.add(item)
        else:
            checados.add(item)
    return list(duplicados)