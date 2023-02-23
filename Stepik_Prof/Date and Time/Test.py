# class A:
#     field1 = 1
#
#     def make_str(self):
#         print(self.field1)
#
#
# class B(A):
#     field2 = 2
#
#     def make_str(self):
#         print(self.field1, self.field2)
#
#
# class C(A):
#     field3 = 3
#
#     def make_str(self):
#         print(self.field1, self.field3)
#
#
# a = A()
# b = B()
# c = C()
#
# for i in (a, b, c):
#     i.make_str()

# class Person:
#     def __init__(self, id):
#         self.id = id
#
#
# some_person = Person(100)
# some_person.__dict__['age'] = 30
# print(some_person.age + len(some_person.__dict__))
#
# print(isinstance(some_person, Person))
#
#
# class Income:
#     def __init__(self, id_):
#         self.id_ = id_
#         id_ = 100
#
#
# income_1 = Income(1000)
# print(income_1.id_)
#
# class A:
#     arg = 'Python'  # Все экземпляры этого класса будут иметь атрибут arg, равный "Python"
#     b = 0
#     c = 0
#
#     def g(self):
#         return self.arg
#
#     def f(self):
#         b = 2
#         c = 2
#         return self.b + self.c
#

# class MyClass:
#     x = 10  # Атрибут объекта класса общий для всех экземпляров
#     y = 5
#
#     def __init__(self, v1, v2):
#         self.x = v1 ** v2
#         print(f'{v1} ** {v2}  = {self.x}')
#
#
# c1 = MyClass(10, 10)  # Создаем первый экземпляр класса
# c2 = MyClass(5, 5)  # Создаем второй экземпляр класса
#
# # Выведем значения атрибута х, а затем изменим значение и опять произведем вывод:
#
# print(c1.x, c2.x)  # Вывод: 10 10
#
# class Class1:
#     # Базовый класс
#     def __init__(self):
#         print("Конструктор базового класса")
#
#     def func1(self):
#         print("Метод funс1() класса Class1")
#
#
# class Class2(Class1):
#     # Класс Class2 наследует класс Classl
#     def __init__(self):
#         print("Конструктор производного класса")
#         Class1.__init__(self)  # Вызываем конструктор базового класса
#
#     def func1(self):
#         print("Метод func1() класса Class2")
#         Class1.func1(self)  # Вызываем метод базового класса
#
#
# c = Class2()  # Создаем экземпляр класса Class2
# c.func1()

from datetime import timedelta


def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60


# Рабочая смена длится 7 часов 30 минут, сколько полных смен в 3-х сутках?
# Решение. Приведенный ниже код решает поставленную задачу:

all_time = timedelta(days=1)
smena = timedelta(hours=7, minutes=30)

print(f'В {all_time.days} сутках - {all_time // smena} смены')
print(f'Остается - {all_time % smena}')
