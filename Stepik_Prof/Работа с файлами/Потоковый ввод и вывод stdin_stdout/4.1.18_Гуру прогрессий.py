"""
Гуру прогрессий
Дана последовательность целых чисел.
Напишите программу, которая определяет, является ли данная последовательность прогрессией,
и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх), в каждой строке
записано натуральное число — очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:
    Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
    Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
    Не прогрессия, если введенная последовательность чисел не является прогрессией

Примечание 1. Гарантируется, что вид прогрессии определяется однозначно.

Sample Input 1:
1
2
3
4
5

Sample Output 1:
Арифметическая прогрессия

Sample Input 2:
2
4
8
16

Sample Output 2:
Геометрическая прогрессия

Sample Input 3:
1
9
1
1
4
5

Sample Output 3:
Не прогрессия
"""
from sys import stdin
# nums = list(map(lambda x: int(x.strip()), stdin))
nums = [int(n.strip()) for n in open(0)]
a = all(map(lambda i: nums[i] - nums[i-1] == nums[1] - nums[0], range(1, len(nums))))
g = all(map(lambda i: nums[i] / nums[i-1] == nums[1] / nums[0], range(1, len(nums))))
print((('Не прогрессия', 'Геометрическая прогрессия')[g], 'Арифметическая прогрессия')[a])


# nums = [int(n.strip()) for n in open(0)]
# l_nums, d, q = len(nums) - 1, nums[1] - nums[0], nums[1] // nums[0]
# flags_ap, flags_gp = False, False
# 
# for i in range(1, len(nums)):
#     if nums[i] - nums[i - 1] == d:
#         flags_ap += True
#     if nums[i] // nums[i - 1] == q:
#         flags_gp += True
# 
# if flags_ap == l_nums:
#     print('Арифметическая прогрессия')
# elif flags_gp == l_nums:
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')
