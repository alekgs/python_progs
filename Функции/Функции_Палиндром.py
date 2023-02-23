def palindrom(word: str) -> bool | None:
    """ Функция проверяет, является ли слово палиндромом
        и возвращает True или False после проверки"""
    if len(word) <= 1:
        return True
    if word[0].lower() != word[-1].lower():
        return False
    return palindrom(word[1:-1])


print(palindrom('Потап'))
print(palindrom('Потоп'))
print(palindrom('ротоР'))
print(palindrom(str(1000)))




