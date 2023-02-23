# Сортировка слиянием (merge sort)

def merge_two_list(a: list, b: list) -> list | None:
    """Функция merge_two_list объединяет два списка """
    i, j, len_a, len_b, res = 0, 0, len(a), len(b), []
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:] + b[j:])
    return res


def merge_sort(s: list) -> list:
    """Функция merge_sort выполняет сортировку методом слияния (merge sort)"""
    len_lst = len(s)
    if len_lst == 1:
        return s
    middle = len_lst // 2
    return merge_two_list(merge_sort(s[:middle]), merge_sort(s[middle:]))


print([6, 2, 19, 5, 10, 7, 11, 3, 0, 21, 76, 99, 35, 22, 90, 101, 15, 18, 11])
print(sorted([6, 2, 19, 5, 10, 7, 11, 3, 0, 21, 76, 99, 35, 22, 90, 101, 15, 18, 11]))
print(merge_sort([6, 2, 19, 5, 10, 7, 11, 3, 0, 21, 76, 99, 35, 22, 90, 101, 15, 18, 11]))
