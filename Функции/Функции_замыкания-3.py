"""
Несколько функций в замыкании

Внутри функции замыкания можно создавать несколько функций, которые будут влиять на вашу общую переменную. Здесь
имеется две вложенные функции increment и decrement. Первая увеличивает общую переменную count, вторая уменьшает.

Данные функцию возвращаются из нашего замыкания

return increment, decrement

здесь не стоит забывать про порядок перечисления этих функций. В данном случае мы возвращаем сперва инкремент,
потом декремент. Поэтому и переменные названы соответствующим образом, в которые записывается результат вызова

inc_1, dec_1 = create_counter()
Порядок можно поменять, но не забывайте тогда и переставлять переменные в моменте
обработки вызова функции create_counter

"""


class create_counter:
    count = 0

    # def __init__(self, total=0):
    #     self.count = total

    def increment(self, value: int = 1):
        self.count += value
        return self.count

    def decrement(self, value: int = 1):
        self.count -= value
        return self.count


res = create_counter()
print(res.increment())  # увеличиваем на 1
print(res.increment(2))  # увеличиваем на 2
print(res.increment(3))  # увеличиваем на 3
print()
print(res.decrement())  # уменьшаем на 1
print(res.decrement(3))  # уменьшаем на 3

print('-' * 15)
print('Создаем новый объект замыкания с другим счетчиком')
res2 = create_counter()

print(res2.increment(10))  # увеличиваем на 10
print(res2.decrement(5))  # уменьшаем на 5
print(res2.increment(100))  # увеличиваем на 100
print(res2.increment(50))  # увеличиваем на 50
print(res2.decrement())  # уменьшаем на 1


def create_counter():
    count = 0

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    return increment, decrement


inc_1, dec_1 = create_counter()
print(inc_1())  # увеличиваем на 1
print(inc_1(2))  # увеличиваем на 2
print(inc_1(3))  # увеличиваем на 3
print(dec_1())  # уменьшаем на 1
print(dec_1(3))  # уменьшаем на 3

print('-' * 15)
print('Создаем новый объект замыкания с другим счетчиком')

inc_2, dec_2 = create_counter()
print(inc_2(10))  # увеличиваем на 10
print(dec_2(5))  # уменьшаем на 5
print(inc_2(100))  # увеличиваем на 100
print(inc_2(50))  # увеличиваем на 50
print(dec_2())  # уменьшаем на 1

