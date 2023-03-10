"""
Дан список с визитами по городам и странам.
Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
"""
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
logs_temp = []
for sl in geo_logs:
    [logs_temp.append(sl) for country in sl.values() if 'Россия' in country]
print(geo_logs := logs_temp)

