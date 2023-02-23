"""
Функция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:
    filename — название csv файла, например, data.csv

Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
а значением — список элементов этого столбца.
Примечание 1.
Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не используются.
Примечание 2.
Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.
Примечание 3.
Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4
Anri,5

то следующий вызов функции csv_columns():
csv_columns('exam.csv')
должен был бы вернуть:
{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.

"""
import csv


# 1
# def csv_columns(filename: str) -> dict or None:
#     """Принимает filename — название csv файла и возвращает словарь,
#        в котором ключом является название столбца файла filename,
#        а значением — список элементов этого столбца
#     """
#     with open(filename, encoding='utf-8') as f:
#         rows, result = list(csv.reader(f, delimiter=',')), {}
#         columns = rows[0]
#         for row in rows[1:]:
#             for i, col_name in enumerate(columns):
#                 result[col_name] = result.get(col_name, []) + [row[i]]
#     return result
#

# 2
def csv_columns(filename: str) -> dict:
    """
    Принимает filename — название csv файла и возвращает словарь,
    в котором ключом является название столбца файла filename,
    а значением — список элементов этого столбца
    """
    with open(filename, encoding='utf-8') as f:
        rows, result = csv.DictReader(f, delimiter=','), {}
        for row in rows:
            for key, value in row.items():
                result[key] = result.get(key, []) + [value]
        return result


print(csv_columns('data.csv'))
