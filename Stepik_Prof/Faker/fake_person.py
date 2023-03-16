from datetime import date
from random import choice

from faker import Faker
from transliterate import translit

faker = Faker('ru_RU')


def calculate_age():
    today = date.today()
    year_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[0])
    month_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[1])
    day_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[2])
    age_t = today.year - year_f - ((today.month, today.day) < (month_f, day_f))
    bith_date = f'{day_f}.{month_f}.{year_f}'
    return age_t, bith_date


def faker_person_create():
    age, b_date = calculate_age()
    credit_card = f'{faker.credit_card_number()}, Срок действия: {faker.credit_card_expire()}, ' \
                  f'CVC-код: {faker.credit_card_security_code()}'
    dict_mail = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@bk.ru']
    name_f = faker.name()
    vk_ur = f'{str(name_f).split()[0].lower()}_{str(name_f).split()[2][:4].lower()}'
    dict_person = {'Ф.И.О.': name_f, 'Дата рождения': b_date, 'Возраст': age, 'Место работы': faker.company(),
                   'Должность': faker.job().lower(), 'Адрес': f'Россия, {faker.address()[0:-8]}',
                   'Почтовый индекс': faker.address()[-6:], 'Телефон': faker.phone_number(),
                   'E-mail': translit(str(name_f).split()[0].lower(), language_code='ru', reversed=True) + \
                             choice(dict_mail),
                   'Профиль VK': "https://vk.com/" + translit(vk_ur, language_code='ru', reversed=True). \
                       replace("'", "").replace(".", ""),
                   'Банковская карта': credit_card}
    return dict_person


def print_person_data(dict_person, i):
    with open('person_faker.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
    for item in dict_person:
        print(f'{item}: {dict_person[item]}')
        with open('person_faker.txt', 'a', encoding='utf-8') as file:
            file.write(f'{item}: {dict_person[item]}\n')


def main():
    print(calculate_age())


if __name__ == '__main__':
    person_count = int(input('\n[+] Введите количество личностей\n    для генерации >>> '))
    for i in range(person_count):
        print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
        dict_person = faker_person_create()
        print_person_data(dict_person, i)
    main()
