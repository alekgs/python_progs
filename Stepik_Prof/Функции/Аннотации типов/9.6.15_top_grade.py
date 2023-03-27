"""
Функция top_grade()

Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по
ключу grades

Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую
оценку по ключу top_grade.

Примечание 2.
В возвращаемом функцией словаре сначала должно следовать имя, а затем — самая высокая оценка.

Sample Input 1:
info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))

Sample Output 1:
{'name': 'Timur', 'top_grade': 99}

Sample Input 2:
print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

Sample Output 2:
{'name': 'Ruslan', 'top_grade': 86}

Sample Input 3:
annotations = top_grade.__annotations__
print(annotations['grades'])

Sample Output 3:
dict[str, str | list[int]]

"""


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    # return {'name': grades['name'], 'top_grade': max(grades['grades'])}

    grades['top_grade'] = max(grades.pop('grades'))
    return grades


info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))

print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

annotations = top_grade.__annotations__
print(annotations['grades'])

# TEST_8:
print(*top_grade.__annotations__.values())
# dict[str, str | list[int]] dict[str, int]
# dict[str, str | list[int]] dict[str, str | int]

# # TEST_9:
info = {'name': 'Roman', 'grades': [40]}
print(top_grade(info))
