# алгоритм бинарного поиска
#
# угадайка наоборот - человек загадывает число в заданном диапазоне,
# а программа пытается его угадать
from math import ceil
from random import randint
import sys
from statistics import mean


def game_body(rounds, difficulty):
    win_round_user = 0
    win_round_comp = 0

    print("Кол-во раундов: ", str(rounds))

    for i in range(1, rounds + 1):
        print("Раунд №" + str(i))
        sum_steps_user = guess_user(difficulty)
        sum_steps_comp = guess_comp(get_middle_number)
        if sum_steps_user < sum_steps_comp:
            win_round_user += 1
        else:
            win_round_comp += 1
    if win_round_comp < win_round_user:
        result = "Победил компьютер!\n"
    elif win_round_comp > win_round_user:
        result = "Победил Пользователь!\n"
    else:
        result = "Ничья!\n"
    return result


def fun_exit(command):
    if command == "exit":
        sys.exit()


def get_middle_number(start, end):
    return (start + end) // 2


def get_random_number(start, end):
    return randint(start, end)


def guess_comp(get_number):
    guess = randint(1, 100)
    step = 1

    print("============================")
    print("Компьютер загадывает число от 1 до 100, вы отгадываете.")

    while True:
        a = input(str(step) + '-я попытка: ')
        fun_exit(a)
        if int(a) > guess:
            print('Меньше')
        elif int(a) < guess:
            print('Больше')
        else:
            print('Вы угадали с %d-й попытки\n' % step)
            break
        step += 1
    return step


def guess(get_number, number):
    start = 1
    end = 100
    steps = 0

    while True:
        a = get_number(start, end)
        steps += 1
        if number < a:
            end = a - 1
        elif number > a:
            start = a + 1
        else:
            break
    print(f'Число {number} отгадано за {steps} шагов')
    return steps


def guess_user(get_number):
    start = 1
    end = 100
    steps = 0

    print("============================")
    print("Вы загадываете число от 1 до 100, компьютер отгадывает.")

    while True:
        a = get_number(start, end)
        print(f'Вы загадали {a}?')
        steps += 1
        answer = input('> ')
        fun_exit(answer)
        if answer.lower() in ('меньше', 'м', 'М', '<', '-'):
            end = a - 1
        elif answer.lower() in ('больше', 'б', 'Б', '>', '+'):
            start = a + 1
        elif answer.lower() == 'да':
            break
        else:
            steps -= 1
            print("Ответ неверный")
    print(f'Отгадано за {steps} шагов\n')
    return steps


def game_vs_comp():
    rounds = input("Введите кол-во раундов (по умолчанию 3).\n> ")

    print("Выберите уровень сложности:")
    print("1 - Лёгкий, компьютер использует более простой, медленный алгоритм угадывания.")
    difficulty_level = input("2 - Сложный, компьютер использует более быстрый, оптимальный алгоритм угадывания.\n> ")

    if rounds == "" or rounds == "3" and difficulty_level == "1":
        result = game_body(3, get_random_number)
        print(result)
    elif rounds == "" or rounds == "3" and difficulty_level == "2":
        result = game_body(3, get_middle_number)
        print(result)
    elif 1 <= int(rounds) and int(rounds) <= 10 and difficulty_level == "1":
        result = game_body(int(rounds), get_random_number)
        print(result)
    elif 1 <= int(rounds) and int(rounds) <= 10 and difficulty_level == "2":
        result = game_body(int(rounds), get_middle_number)
        print(result)
    else:
        print("Количество раундов можно выбрать от 1 до 10")


def random_numbers(col_num):
    nums = []
    for i in range(col_num):
        nums.append(randint(1, 100))
    return nums


def test_method(method, numbers):
    results = []
    for i in numbers:
        res = guess(method, i)
        results.append(res)
    return mean(results)


def common_test_method():
    numbers = random_numbers(int(input("Введите количество чисел:\n")))

    print(f'Тестирую метод: Бинарный поиск')
    middle_avg = float(test_method(get_middle_number, numbers))

    print(f'\nТестирую метод: Рандом')
    random_avg = float(test_method(get_random_number, numbers))

    print("\nСреднее кол-во шагов методом 'Бинарный поиск' - " + str(round(middle_avg, 2)))
    print("Среднее кол-во шагов методом 'Рандом' - " + str(round(random_avg, 2)))

    if middle_avg < random_avg:
        print("\nРезультат теста - Бинарный поиск быстрее\n")
    elif middle_avg > random_avg:
        print("\nРезультат теста - Рандом быстрее\n")
    else:
        print("\nРезультат теста - Одинаково\n")


while True:
    print("============================")
    print("Выберите режим игры 1 или 2 или 3 или 4:")
    print("1. Режим - Компьютер отгадывает число.")
    print("2. Режим - Игра наоборот, пользователь отгадывает число.")
    print("3. Режим - Игра по очереди против компьютера.")
    print("4. Режим - Тестирования методов 'Рандом' и 'Бинарный поиск'.")

    choose = input(">>  Введите 'exit' для выхода, в любой момент\n> ")

    if choose == '1':
        guess_user(get_middle_number)
    elif choose == '2':
        guess_comp(get_random_number)
    elif choose == '3':
        game_vs_comp()
    elif choose == '4':
        common_test_method()
    elif choose in ('exit', 'quit', 'bye'):
        break
    else:
        print('Вы ввели неправильную команду\n')

