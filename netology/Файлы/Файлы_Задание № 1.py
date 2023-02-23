"""
Необходимо написать программу для кулинарной книги.
Список рецептов должен храниться в отдельном файле в следующем формате:

Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения
...

Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт

В одном файле может быть произвольное количество блюд.
Читать список рецептов из этого файла.
Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.


Задача №1
Должен получится следующий словарь

cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'},
    {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'},
    {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'},
    {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]
    }
"""
from pprint import pprint


def make_cookbook(f='recipes.txt') -> dict:
    """Функция преобразует текстовый файл в словарь - книгу рецептов"""
    cook_book = {}
    try:
        with open(f, encoding='utf-8') as file:
            for recipe_name in file:
                recipe_name = recipe_name.strip('\n')
                for _ in range(int(file.readline().strip('\n'))):
                    ingredients = {}
                    list_ingredients = file.readline().strip('\n').split(' | ')
                    ingredients['ingredient_name'] = list_ingredients[0]
                    ingredients['quantity'] = list_ingredients[1]
                    ingredients['measure'] = list_ingredients[2]
                    cook_book[recipe_name] = cook_book.get(recipe_name, []) + [ingredients]
                file.readline()
    except FileNotFoundError:
        print(f"Файл '{f}' не найден")
    return cook_book


# testing
pprint(make_cookbook(), sort_dicts=True)


