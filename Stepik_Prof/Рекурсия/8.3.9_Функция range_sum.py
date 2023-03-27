"""
Функция range_sum()

Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:
    numbers — список целых чисел
    start — целое неотрицательное число
    end — целое неотрицательное число

Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно и возвращать
полученный результат.

Примечание 1.

Рассмотрим первый тест. Диапазону индексов [3;7] в переданном списке принадлежат числа 4,5,6,7,8
сумма которых равна: 4+5+6+7+8=30

Примечание 2. Гарантируется, что start <= end.

Sample Input 1:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

Sample Output 1:
30

Sample Input 2:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))

Sample Output 2:
45

Sample Input 3:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))

Sample Output 3:
1
"""


# замыкание
# def range_sum(numbers, start, end):
#     def closure(step):
#         if step == end:
#             return numbers[end]
#         return numbers[step] + closure(step + 1)
#     return closure(start)

def range_sum(numbers, start, end):
    if start > end:
        return 0
    return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
