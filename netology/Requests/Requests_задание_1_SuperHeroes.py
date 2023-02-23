"""
Задача № 1 Кто самый умный супергерой?
Есть API по информации о супергероях с информацией по всем супергероям.
Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
"""
import requests

result = []
try:
    print('Подключаемся к серверу...', end='')
    resp = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    if resp.status_code == 200:
        print('OK')
        print('Выбираем супергероев: Hulk, Captain America, Thanos...', end='')
        for s in resp.json():
            if s['name'] in ('Hulk', 'Captain America', 'Thanos'):
                result.append((s['name'], s['powerstats']['intelligence']))
        print('OK')
    else:
        print(f"Ошибка получения даннных с сервера")
        print(f"Response status code: {resp.status_code}")
except requests.RequestException:
    print('Ошибка подключения к серверу')

name, max_intelligence = max(result, key=lambda x: x[1])
print(f'Самый умный из трех супергероев Hulk, Captain America, Thanos: {name} (skill - {max_intelligence})')

