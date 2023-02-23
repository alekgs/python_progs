"""
Элементы JSON

Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение
этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение
двоеточием, каждую на отдельной строке. Если значением ключа является список, то все его элементы должны быть
выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.
Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.


Sample Input 1:

{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}

Sample Output 1:

size: 36
style: bold
name: text1
alignment: center

Sample Input 2:

{
 "type": "donut",
 "name": "Cake",
 "tastes": ["chocolate", "cream", "strawberry"]
}

Sample Output 2:

type: donut
name: Cake
tastes: chocolate, cream, strawberry


"""
import json

# str_json = json.loads(''.join([s.strip() for s in open(0)]))

str_json = json.loads(open(0).read())
for k, v in str_json.items():
    print(f"{k}: {', '.join(map(str, v)) if isinstance(v, list) else v}")




