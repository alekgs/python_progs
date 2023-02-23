# Если введенное число меньше загаданного числа, выведите текст: 'Ваше число меньше загаданного, попробуйте еще разок';
# Если введенное число больше загаданного числа, выведите текст: 'Ваше число больше загаданного, попробуйте еще разок';
# Если введенное число равно загаданному числу, выведите текст: 'Вы угадали, поздравляем!'.
# Выведите прощальное сообщение пользователю: 'Спасибо, что играли в числовую угадайку. Еще увидимся...'.
# количество гарантированных шагов для угадывания

from random import *


# функция проверки вводимого числа на цифровое значение и соответствие диапазону
def is_valid(n, x, y):  # проверка на соответствие введенного значения условию
    return n.isdigit() and x <= int(n) <= y


# ввод данных
def input_num(down_num=1, up_num=1000):
    while True:
        guess = input()
        if is_valid(guess, down_num, up_num):
            return int(guess)
        else:
            print(f'А может быть все-таки введем целое число от {down_num} до {up_num}?')


# сравнение чисел
def compare_num(down_num, up_num):
    # "загадываем" случайное число для угадывания
    num_rand = randint(down_num, up_num)
    total = 0
    while True:
        inp_num = input_num()
        total += 1
        if inp_num < num_rand:
            print('Ваше число меньше загаданного, попробуйте еще разок:')
        elif inp_num > num_rand:
            print('Ваше число больше загаданного, попробуйте еще разок:')
        else:
            print(f'Вы угадали число с {total}-й попытки, поздравляем!')
            break


# Предложение продолжить игру
def continue_game():
    ans = input('Хотите продолжить (Д/Н)?: ')
    while True:
        if ans not in ('y', 'Y', 'д', 'Д', 'n', 'N', 'н', 'Н'):
            ans = input('Ответ неверный...\nПродолжим (Д/Н)?: ')
        elif ans in ('n', 'н'):
            print('До свидания!')
            return False
        else:
            return True


# Запуск игры
def begin_game():
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа')
        print('от:', end=' ')
        x = input_num()
        print('до:', end=' ')
        y = input_num()
        if x > y:
            x, y = y, x
        print('Введите ваше число от', x, 'до', y, ':', end=' ')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


begin_game()
