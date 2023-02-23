def flatten(lst: list) -> list | None:
    """Превращает вложенные списки в линейный"""
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])


print(flatten([1, [2, 3, [4]], 5]))  # => [1, 2, 3, 4, 5]
print(flatten([1, [2, 3], [[2], 5], 6]))  # => [1, 2, 3, 2, 5, 6]
print(flatten([[[[9]]], [1, 2], [[8]]]))  # => [9, 1, 2, 8]
