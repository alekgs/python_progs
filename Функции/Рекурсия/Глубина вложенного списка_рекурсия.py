def list_level_recursion(lst: list, level: int = 1):
    """Функция принимает на вход список вложенных списков и возвращает их уровни вложения"""
    print(*lst, f'level = {level}')
    for i in lst:
        if type(i) == list:
            list_level_recursion(i, level + 1)
    return


a = [1, [3, [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
list_level_recursion(a)
