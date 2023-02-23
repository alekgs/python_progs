# script.py
import os
import pathlib
from sys import platform

DIR = pathlib.Path(__file__).parent.resolve()  # текущая директория
tests = os.path.join(DIR, 'tests')
try:
    n_tests = len(os.listdir(tests)) // 2  # проверяем есть ли папка tests и файл 'code.py'
    open('code.py')
except FileNotFoundError as error:
    print('-' * 69, '\nОШИБКА 404')
    print('Папка с тестами должна называться - tests, а файл с кодом - code.py', '-' * 69, sep='\n')
    raise

python_version = 'py'

for i in range(1, n_tests + 1):
    with open(os.path.join(tests, str(i))) as test, open(os.path.join(tests, f'{str(i)}.clue')) as clue:
        result = os.popen(f"{python_version} code.py < {os.path.join(tests, str(i))}").read().strip()
        correct = clue.read()
        assert result == correct, f"Test#{i}\n{'-' * 69}\nexpect:{repr(correct)}\nresult:{repr(result)}\n"
    print(f'Test#{i} PASSED')
print(f'Всё в порядке!Проверено {n_tests} шт.')
