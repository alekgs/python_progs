# объявление функции
def get_month(language, number):
    en_month = ['january', 'February', 'march', 'april', 'may', 'june', 'jule', 'august', 'september', 'october',
                'november', 'december']
    ru_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
                'октябрь', 'ноябрь', 'декабрь']
    return ru_month[number - 1] if language == 'ru' else en_month[number - 1]


# считываем данные2
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
