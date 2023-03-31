import sys, time


def teleprint(*args, delay=0.05, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        print(char, end='')
        time.sleep(delay)


teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
