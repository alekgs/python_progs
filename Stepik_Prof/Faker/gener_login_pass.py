# from faker import Faker
# from random_username.generate import generate_username
#
#
# faker = Faker('ru_RU')
#
# for i in range(10):
#     print(f'Логин: {generate_username()[0]}')
#     print(f'Пароль: {faker.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True)}\n')

from mimesis import Person
from mimesis.locales import Locale


# person = Person(Locale.RU)
person = Person()
for i in range(10):
    print(f"Логин: {person.username(mask='l_d', drange=(1800, 2100))}")
    print(f"Пароль: {person.password(length=16, hashed=False)}\n")
