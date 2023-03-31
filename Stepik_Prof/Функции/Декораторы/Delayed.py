"""
Декоратор delayed

Реализуем декоратор delayed, который создает требуемую задержку выполнения кода.
Такое поведение иногда требуется для мониторинга доступности какого-нибудь ресурса.
"""

import functools
import time


def delayed(delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'\n>>> cпим {delay} сек.', end='')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@delayed(1)
def countdown(number):
    if number < 1:
        print('\rКонец!')
    else:
        print(f'\rRetry: {number}', end='')
        countdown(number - 1)


countdown(5)
