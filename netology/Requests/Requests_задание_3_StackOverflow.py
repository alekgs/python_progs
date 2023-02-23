"""
Самый важный сайт для программистов это stackoverflow. И у него тоже есть API
Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'.
Для этого задания токен не требуется.
"""
import requests
from datetime import datetime, timedelta

headers = {
           "Accept": "application/json",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
           }
questions_url = 'https://api.stackexchange.com/2.3/questions'

today = datetime.today()
fr_date = today - timedelta(days=1)

from_date = int(fr_date.timestamp())
to_date = int(today.timestamp())

params = {
          "fromdate": from_date,
          "todate": to_date,
          "order": "asc",
          "tagged": "python",
          "sort": "creation",
          "site": "stackoverflow"
          # "filter": "!nOedRLb*F("
          }

response = requests.get(questions_url, params=params, headers=headers).json()

mask = '%d.%m.%Y %H:%M'
today = today.strftime(mask)
fr_date = fr_date.strftime(mask)

result = []
print('Список вопросов сайта Stackoverflow.com за последние 2 дня')
print(f'(с {fr_date} по {today})')
print()

for item in response.get('items'):
    creat_date = datetime.fromtimestamp(int(item['creation_date'])).strftime(mask)
    print(f"Creation date: {creat_date}")
    print(f"User: {item['owner']['display_name']}")
    print('Tags: ' + ', '.join(item['tags']))
    print(item['link'])
    print(f"Question: {item['title']}")
    # print(f"Question body: {item['body_markdown']}")
    print()
