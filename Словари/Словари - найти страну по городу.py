"""
Переменные countries соединяют ряд стран с тремя крупнейшими городами каждой страны.
Программе на вход будет поступать название города в переменную city.
И ваша задача найти какой стране принадлежит введенный город.
Если страна успешно найдена, необходимо вывести сообщение:
INFO: <City> is a city in <Country>

в противном случае
ERROR: Country for {City} not found

Учитывайте, что регистр букв имеет значение
"""
countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
city = input()
for country, cities in countries.items():
    if city in cities:
        print(f'INFO: {city} is a city in {country}')
        break
else:
    print(f'ERROR: Country for {city} not found')
