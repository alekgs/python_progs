"""
Задача №2

У Яндекс.Диска есть очень удобное и простое API.
Для описания всех его методов существует Полигон.
Нужно написать программу, которая принимает на вход путь до файла на компьютере
и сохраняет на Яндекс.Диск с таким же именем.

Все ответы приходят в формате json;
Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".

HOST: https://cloud-api.yandex.net:443
Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!
"""
import requests


class YaUploader:
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Accept": "application/json", "Authorization": f"{self.token}"}

    def get_upload_link(self, file_path) -> str or bool:
        """Получает и возвращает ссылку от сервера на загрузку файла """
        params = {"path": file_path, "overwrite": "true"}
        print('Получаем ссылку на загрузку файла...', end='')
        resp = requests.get(self.upload_url, params=params, headers=self.headers)
        if resp.status_code == 200:
            href = resp.json().get('href')
            print('OK')
            return href
        else:
            print('Ошибка')
            print('Не удалось получить ссылку на загрузку файла')
            print(f"Error {resp.status_code}: {resp.json().get('description')}")
            return False

    def upload_file(self, file_path):
        """Производит загрузку файла на сервер Я.Диск"""
        try:
            href = self.get_upload_link(file_path)
            if href:
                with open(file_path, "rb") as f:
                    print('Загружаем файл на сервер...', end='')
                    response = requests.put(href, data=f)
                    if response.status_code == 201:
                        print('OK')
                        print(f"Файл '{file_path}' успешно загружен на Я.Диск")
                        return True
                    print("\nОшибка при загрузке файла")
                    print(f"Error {response.status_code}: {response.json().get('description')}")
            return False
        except requests.RequestException:
            print('\nОшибка подключения к серверу')


if __name__ == '__main__':

    file_token = 'token.txt'
    file_upload = 'test.py'

    with open(file_token) as f_token:
        uploader = YaUploader(f_token.readline().strip())
    result = uploader.upload_file(file_upload)
