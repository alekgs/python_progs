"""
Сериализация словаря
Ваша задача выполнить сериализацию словаря и сохранить полученную json-строку
в переменную json_data. В качестве ответа распечатайте значение переменной json_data
"""

from string import ascii_lowercase
import json

print(json_data := json.dumps({ascii_lowercase[i]: i + 1 for i in range(26)}))
