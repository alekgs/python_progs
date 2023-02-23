"""
Быстрая сортировка - quicksort

"""


# функция быстрой сортировки - quicksort
def quicksort(array):
    if len(array) < 2:  # если список пуст или из одного элемента, то не сортируем и возвращаем
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


# n = int(input())  # количество элементов списка
lst = list(map(int, input().split()))  # список для сортировки
print(quicksort(lst))
