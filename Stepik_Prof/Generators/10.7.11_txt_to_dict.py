"""
Функция txt_to_dict()

Вам доступен файл planets.txt, содержащий информацию о различных планетах.
В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка,
затем характеристики второй планеты, и так далее:

Name = Mercury
Diameter = 4879.4
Mass = 3.302×10^23
OrbitalPeriod = 0.241

Name = Venus
Diameter = 12103.6
Mass = 4.869×10^24
OrbitalPeriod = 0.615

...

Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий последовательность словарей,
каждый из которых содержит информацию об очередной планете из файла planets.txt,
а именно ее название, диаметр, массу и орбитальный период.

Например:
{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
"""


def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        lines = (line.strip() for line in file)
        pairs = (tuple(map(str.strip, line.split('='))) for line in lines if len(line))
        yield from (dict(keys_values) for keys_values in zip(pairs, pairs, pairs, pairs))

# def txt_to_dict():
#     with open('planets.txt', encoding='utf-8') as file:
#         return (
#                 dict(i.split(' = ') for i in x.split('\n'))
#                 for x in file.read().split('\n\n')
#                 )


# def txt_to_dict():
#     with open('planets.txt', encoding='utf-8') as f:
#         # ['Name = Mercury', 'Diameter = 4879.4', 'Mass = 3.302×10^23', 'OrbitalPeriod = 0.241']
#         planets = (planet.split('\n') for planet in f.read().split('\n\n'))
#
#         # [['Name', 'Mercury'], ['Diameter', '4879.4'], ['Mass', '3.302×10^23'],
#         # ['OrbitalPeriod', '0.241']]
#         planets_info = ((p.split(' = ') for p in planet) for planet in planets)
#
#     # преобразование объектов генератора в словари согласно условию
#     for p in planets_info:
#         yield dict(p)


planets = txt_to_dict()
print(next(planets))

# Sample Output:
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

# TEST_2:
planets = txt_to_dict()
print(*planets)

# TEST_2:
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod':
# '0.241'} {'Name': 'Venus', 'Diameter': '12103.6', 'Mass': '4.869×10^24', 'OrbitalPeriod':
# '0.615'} {'Name': 'Earth', 'Diameter': '12756.3', 'Mass': '5.974×10^24', 'OrbitalPeriod': '1'}
# {'Name': 'Mars', 'Diameter': '6794.4', 'Mass': '6.419×10^23', 'OrbitalPeriod': '1.881'} {
# 'Name': 'Jupiter', 'Diameter': '142984', 'Mass': '1.899×10^27', 'OrbitalPeriod': '11.86'} {
# 'Name': 'Saturn', 'Diameter': '120536', 'Mass': '5.688×10^26', 'OrbitalPeriod': '29.46'} {
# 'Name': 'Uranus', 'Diameter': '51118', 'Mass': '8.683×10^25', 'OrbitalPeriod': '84.01'} {
# 'Name': 'Neptune', 'Diameter': '49572', 'Mass': '1.024×10^26', 'OrbitalPeriod': '164.79'} {
# 'Name': 'Pluton', 'Diameter': '2370.0', 'Mass': '1.3×10^22', 'OrbitalPeriod': '247.7406624'}
