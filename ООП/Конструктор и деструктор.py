"""
Напишите программу по следующему описанию:
1. Есть класс Person, конструктор которого принимает три параметра (не учитывая self) –
имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по
умолчанию, равное единице.
2. У класса Person есть метод, который возвращает строку, включающую в себя всю
информацию о сотруднике.
3. Класс Person содержит деструктор, который выводит на экран фразу "До свидания,
мистер …" (вместо троеточия должны выводиться имя и фамилия объекта).
4. В основной ветке программы создайте три объекта класса Person. Посмотрите
информацию о сотрудниках и увольте самое слабое звено.
5. В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не
будет нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении
работы программы.
"""


class Person:
    # persons = []

    def __init__(self, name, surname, quality=1):
        self.name = name
        self.surname = surname
        self.quality = quality
        # Person.persons.append({'obj': self, 'name': self.name, 'surname': self.surname, 'quality': self.quality})

    def info(self):
        print(f'Name: {self.name:>7}')
        print(f'Surname: {self.surname}')
        print(f'Quality: {self.quality}')
        print()

    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}')

    # Метод возвращает кортеж из имени объекта и self
    # def get_name(self):
    #     return [(name_obj, obj) for name_obj, obj in globals().items() if obj is self][0]


pers = [Person('John', 'Doe', 10), Person('Sara', 'Connor', 8), Person('Mick', 'Ruby', 5), Person('Real', 'McKoy', 2)]
[p.info() for p in pers]
pers.sort(key=lambda x: x.quality, reverse=True)
del pers[-1]
# [p.info() for p in pers]

input()
# print(pers)
# print(globals().items())
# min_pers_qlty = min(Person.persons, key=lambda x: x['quality'])


# print(f"Minimal quality person: {min_pers_qlty['name']} {min_pers_qlty['surname']} ({min_pers_qlty['quality']})")

# Получаем имя этого объекта
# name, obj_name = min_pers_qlty['obj'].get_name()
# print(f'Deleting object "{name}" from class Person...')

# print(obj_name)

# Проверяем удалился или нет этот объект
# person3.info()
# print(globals().items())
# obj_name.info()
# input()
