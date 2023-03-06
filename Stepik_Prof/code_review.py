def get_max_index(numbers):
    max_index = 0
    max_value = numbers[-1]

    for index, value in enumerate(numbers):
        if value >= max_value:
            max_index = index
            max_value = value

    return max_index


print(get_max_index([1, 2, 3, 4, 5, 6, 17, 8, 9, 19]))
