"""
Функция cyclic_shift()

Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает
два аргумента в следующем порядке:

    numbers — список целых или вещественных чисел
    step — целое число

Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов,
и возвращать значение None. Если step является положительным числом, сдвиг происходит вправо,
если отрицательным — влево.


Sample Output 1:
[5, 1, 2, 3, 4]


Sample Output 2:
[3, 4, 5, 1, 2]
"""


def cyclic_shift(nums: list[int | float], step: int) -> None:
    # 1
    step %= len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]

    # 2
    # if step < 0:
    #     for _ in range(abs(step)):
    #         nums.append(nums.pop(0))
    # else:
    #     for _ in range(step):
    #         nums.insert(0, nums.pop())


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)

# TEST_10:
numbers = [234, 235]
cyclic_shift(numbers, 15)
print(numbers)

# TEST_10:
# [235, 234]

# TEST_11:
numbers = [234, 235]
cyclic_shift(numbers, -22)
print(numbers)

# TEST_11:
# [234, 235]