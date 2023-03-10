"""
Юный математик 🌶️

Дима учится в седьмом классе, и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем.
Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя,
и несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.
Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с правильными
несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число nn. Напишите программу, которая находит наибольшую правильную
несократимую дробь с суммой числителя и знаменателя равной nn.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух
чисел. Функция реализована в модуле math.

Тестовые данные 🟢

Sample Input 1:
10
Sample Output 1:
3/7

Sample Input 2:
23
Sample Output 2:
11/12

Sample Input 3:
3
Sample Output 3:
1/2
"""
from fractions import Fraction as F
from math import gcd

n = int(input())

for i in range((n - 1) // 2, 0, -1):
    if gcd(i, n - i) == 1:
        print(F(i, n - i))
        break

# способ № 2
# i = n // 2
# while F(i, n - i).numerator != i:
#     i -= 1
# print(f'{i}/{n - i}')

# способ № 3
# n = int(input())
# i = n // 2
# while gcd(i, n - i) != 1:
#     i -= 1
# print(f'{i}/{n - i}')

# 
# Алекс Глозман
# 7 месяцев назад

# Версия №5. Аналитика.
# 
#  Логика первого слагаемого (n - 1) // 2 заключается в том, что для нечетного 
# числа nn дробь n//2n−n//2n−n//2n//2 удовлетворяет всем необходимым свойствам. А вот для четного слагаемого дробь
# n//2n−n//2n−n//2n//2 потребует вычитания как минимум единицы из числителя (в числителе и знаменателе одинаковые
# числа). Для этих целей как нельзя лучше подходит формула округления до меньшего целого. Остается только учесть 
# особый случай, когда четное число nn при целочисленном делении на 2 дает нечетное число, потому что в этом случае, 
# после вычитания единицы из числителя, образуется сократимая дробь с четными числами в числителе и знаменателе. Как 
# в случае с числом 10: 4 / 6. Тут необходимо вычесть из числителя дополнительную единицу. Для этого служит второе 
# слагаемое или точнее вычитаемое :).  Выражение n & 3 выделяет два младших бита двоичного представления числа nn,  
# число 3 служит маской (310=000...000112310 =000...000112). Если выделенные биты это 102=210102=210,
# то это означает что число делится на 2, но не делится на 4 - наш особый случай.

# num = (n - 1) // 2 - (n & 3 == 2)
# den = n - num
# print(f'{num}/{den}')

