def buscaLinear(arr):
    i = 0
    indice_h = 0
    while i < len(arr):
        if indice_h <= arr[i]:
            indice_h += 1
            i += 1
        else:
            return i

def buscaBinaria(lista):
    inicio = 0
    fim = len(lista) - 1
    indice_h = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] >= meio + 1:
            indice_h = meio + 1
            inicio = meio + 1
        else:
            fim = meio - 1

    return indice_h


arr = [34,18,17,14,3,1,1]
j = buscaBinaria(arr)
print(j)

