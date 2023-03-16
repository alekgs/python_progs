from datetime import date
from random import choice
from mimesis import Person, Address, Finance, Transport, Payment
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale


def create_fake_person():
    address = Address(Locale.RU)
    fin = Finance(Locale.RU)
    person = Person(Locale.RU)
    pay = Payment()
    transport = Transport()
    ru_spec = RussiaSpecProvider()

    mail_dict = ['mail.ru', 'gmail.com', 'rambler.ru', 'yandex.ru', 'hotmail.com', 'outlook.com', 'ya.ru', 'yahoo.com',
                 'mail.com', 'protonmail.com']
    age_pers = person.age(minimum=22, maximum=66)

    dict_person = {'Ф.И.О.': f'{person.first_name(gender=Gender.MALE)} {ru_spec.patronymic(gender=Gender.MALE)} ' \
                             f'{person.last_name(gender=Gender.MALE)}', 'Год рождения': date.today().year - age_pers,
                   'Возраст': age_pers, 'Адрес': f'{address.postal_code()}, {address.city()}, {address.address()}',
                   'Номер телефона': person.telephone(mask='+7-9##-###-####'),
                   'E-mail': person.email(domains=[choice(mail_dict)]), 'Паспорт': ru_spec.series_and_number(),
                   'ИНН': ru_spec.inn(), 'СНИЛС': ru_spec.snils(),
                   'Банковская карта': f'{pay.credit_card_number(card_type=None)}, ' \
                                       f'{pay.credit_card_expiration_date(minimum=23, maximum=27)}, {pay.cvv()}',
                   'Автомобиль': transport.car(), 'Образование': person.university(),
                   'Место работы': f'{fin.company_type(abbr=True)} {fin.company()}',
                   'Должность': person.occupation().lower(), 'Политические взгляды': person.political_views().lower(),
                   'Мировоззрение': person.worldview().lower(), 'Вес': person.weight(minimum=55, maximum=120),
                   'Группа крови': person.blood_type(), 'Логин': person.username(mask='l_Cd', drange=(1800, 2100)),
                   'Пароль': person.password(length=16, hashed=False)}
    return dict_person


def print_person(dict_person, i):
    with open('person_mimesis.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
    for item in dict_person:
        print(f'{item}: {dict_person[item]}')
        with open('person_mimesis.txt', 'a', encoding='utf-8') as file:
            file.write(f'{item}: {dict_person[item]}\n')


def main():
    person_count = int(input('\n[+] Введите количество личностей\n    для генерации >>> '))
    for i in range(person_count):
        print(f'\n{"-" * 16} {i + 1} {"-" * 16}\n')
        dict_person = create_fake_person()
        print_person(dict_person, i)


if __name__ == "__main__":
    main()
