def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def buscaLinear(arr, alvo):
    i = 0
    while i < len(arr) and arr[i] <= alvo:
        if alvo == arr[i]:
            return i
        i += 1
    return i

def buscaBinaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return meio

alvo = int(input())
arr = [3,2,4,9,7,4]

quicksort(arr)

i = buscaLinear(arr,alvo)
print(i)
print(arr)

