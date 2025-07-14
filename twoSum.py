def two_sum_bruto(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_hash_map(arr, alvo):
    chaveValor = {}
    for i, valor in enumerate(arr):
        complemento = alvo - valor
        if complemento in chaveValor:
            return [chaveValor[complemento], i]
        chaveValor[valor] = i

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


def two_sum_quick(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        soma = lista[inicio] + lista[fim]
        if soma == alvo:
            return [inicio, fim]
        elif soma < alvo:
            inicio += 1
        else:
            fim -= 1
    return None


nums = [2, 7, 11, 15]
target = 9

print(two_sum_bruto(nums, target)) 
print(two_sum_quick(nums, target)) 
print(two_sum_hash_map(nums, target))



