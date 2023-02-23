"""
Задача №2

Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон
для кого мы будем готовить

get_shop_list_by_dishes(dishes, person_count)

На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.
Например, для такого вызова

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

Должен быть следующий результат:
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}

Обратите внимание, что ингредиенты могут повторяться
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


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict or str:
    """
    Функция принимает список блюд из cook_book и количество персон и
    возвращает словарь с названием ингредиентов и его количества для блюда
    """
    cook_book = make_cookbook()
    if cook_book:
        calc_ingredients = {}
        for recipe_order in dishes:
            if cook_book.get(recipe_order, None):
                for recipe in cook_book[recipe_order]:
                    i_name = recipe['ingredient_name']
                    i_dict = {'measure': recipe['measure'], 'quantity': int(recipe['quantity']) * person_count}
                    if calc_ingredients.get(i_name):
                        calc_ingredients[i_name]['quantity'] += i_dict['quantity']
                    else:
                        calc_ingredients[i_name] = i_dict
            else:
                print(f'"{recipe_order}": к сожалению, такого рецепта у нас нет')
        return calc_ingredients
    else:
        return 'Не могу создать CookBook'


# testing
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=True)
