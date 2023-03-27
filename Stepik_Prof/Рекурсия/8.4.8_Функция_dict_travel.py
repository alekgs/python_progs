"""
Функция dict_travel() 🌶️🌶️

Реализуйте функцию dict_travel(), которая принимает один аргумент:
    nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь,
    так же содержат в качестве значений числа, строки или словари; вложенность может быть произвольной

Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня,
разделяя их точками.

Например, в словаре:
{'name': 'Arthur', 'grades': {'math': [4, 4], 'chemistry': [3, 4]}}

значение [4, 4] должно быть выведено в следующем формате:
grades.math: [4, 4]

Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.

Примечание 1.
Гарантируется, что ключами в подаваемом в функцию словаре являются строки, содержащие только латинские
буквы в нижнем регистре.

Примечание 2.
Гарантируется, что ни один ключ в подаваемом в функцию словаре не является последовательностью других
ключей. Другими словами, словарь не может иметь, например, следующий вид:
{'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
"""


# def dict_travel(d, path=None):
#     if path is None:
#         path = []
#
#     for k, v in sorted(d.items()):
#         if isinstance(v, dict):
#             dict_travel(v, path + [k])
#         else:
#             print(f"{'.'.join(path + [k])}: {v}")


# def dict_travel(d):
#     for k, v in sorted(d.items()):
#         if isinstance(v, dict):
#             dict_travel({f'{k}.{key}': val for key, val in v.items()})
#         else:
#             print(f'{k}: {v}')

def dict_travel(nested_dicts: dict):
    path = []

    def rec(n_d, p):
        for key, value in sorted(n_d.items()):
            if isinstance(value, dict):
                rec(value, p + [key])
            else:
                print('.'.join(p + [key]) + ':', value)

    rec(nested_dicts, path)





print('# TEST_1')
data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)
# a: 1
# b.a: 10
# b.b: 20
# b.c: 30
print()
print('# TEST_2')
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
dict_travel(data)
# a: 100
# b.a: 10
# b.b: 20
# b.c: 30
# d: 1
print()
print('# TEST_3')
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)
# b.a: 10
# b.b.d: 40
# b.b.e: 50
# b.c: 30
print()
print('# TEST_4')
# TEST_4:
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
dict_travel(data)
# birthday.day: 24
# birthday.month: March
# birthday.year: 1974
# firstname: Alyson
# lastname: Hannigan
print()
print('# TEST_5')
data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                    'postalcode': '125315'}}

dict_travel(data)

# address.city.cityname: Москва
# address.city.region: Московская область
# address.city.type: город
# address.postalcode: 125315
# address.streetaddress: Часовая 25, кв. 127
# birthdate.day: 10
# birthdate.month: October
# birthdate.year: 1993
# firstname: Тимур
# lastname: Гуев
