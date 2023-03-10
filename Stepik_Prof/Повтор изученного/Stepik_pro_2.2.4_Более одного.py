"""
Более одного
Дана последовательность неотрицательных целых чисел.
Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза,
разделяя их пробелом.
Числа должны быть расположены в порядке возрастания и не должны повторяться.

Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить.

"""
# ###### Мой вариант )
d = {}
for i in map(int, input().split()):
    d[i] = d.get(i, 0) + 1
print(*sorted(filter(lambda n: d[n] > 1, d)))
# [print(k, end=' ') for k, v in sorted(d.items()) if v > 1]

# #### через Counter
# data = __import__('collections').Counter(map(int, input().split()))
# print(*sorted(filter(lambda i: data[i] > 1, data)))

# #### Тимур Гуев через множество
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))
