"""
Итоговая работа по модулю "Основы языка программирования"
Задание
Вопросы по заданию

Возможна такая ситуация, что мы хотим показать друзьям фотографии из социальных сетей, но соц. сети могут быть
недоступны по каким-либо причинам. Давайте защитимся от такого. Нужно написать программу для резервного копирования
фотографий с профиля(аватарок) пользователя vk в облачное хранилище Яндекс.Диск. Для названий фотографий использовать
количество лайков, если количество лайков одинаково, то добавить дату загрузки. Информацию по сохраненным фотографиям
сохранить в json-файл.

Задание:
Нужно написать программу, которая будет:

    Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
    Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
    Для имени фотографий использовать количество лайков.
    Сохранять информацию по фотографиям в json-файл с результатами.

Входные данные:

Пользователь вводит:
    - id пользователя vk;
    - токен с Полигона Яндекс.Диска

Выходные данные:
    json-файл с информацией по файлу:

1234
    [{
    "file_name": "34.jpg",
    "size": "z"
    }]

Измененный Я.диск, куда добавились фотографии

Обязательные требования к программе:
    Использовать REST API Я.Диска и ключ, полученный с полигона.
    Для загруженных фотографий нужно создать свою папку.
    Сохранять указанное количество фотографий(по умолчанию 5) наибольшего размера (ширина/высота в пикселях) на Я.Диске
    Сделать прогресс-бар или логирование для отслеживания процесса программы.
    Код программы должен удовлетворять PEP8.
    У программы должен быть свой отдельный репозиторий.
    Все зависимости должны быть указаны в файле requiremеnts.txt

Необязательные требования к программе:
    Сохранять фотографии и из других альбомов.
    Сохранять фотографии на Google.Drive.
"""
import requests
import json
from datetime import datetime as dt
from alive_progress import alive_bar as pbar


class VK:
    url = 'https://api.vk.com/method/photos.get'
    url_user_get = 'https://api.vk.com/method/users.get'

    def __init__(self, token, u_id, a_id, dir_yadisk, version='5.131'):
        self.token = token
        self.id = u_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        self.album_id = a_id
        self.dir_yadisk = dir_yadisk

    @staticmethod
    def get_error_code(rsp):
        if 'error' in rsp.json().keys():
            err_code = rsp.json()['error']['error_code']
            err_msg = rsp.json()['error']['error_msg']
            print(f'\nОшибка получения данных !\n{err_code}: {err_msg}')
            return False
        return True

    def get_user_info(self):
        print(f'\nПолучаем информацию по {self.id}...', end='')
        params = {'user_ids': self.id, 'fields': 'screen_name'}
        resp = requests.post(self.url_user_get, params={**self.params, **params})
        if resp.status_code == 200:
            if not self.get_error_code(resp):
                return 'Error'
            print('OK')
            u_info = resp.json()['response'][0]
            self.id = u_info['id']
            return print(f"id:{u_info['id']} ({u_info['screen_name']}), {u_info['first_name']} {u_info['last_name']}")

    def get_user_photo(self):
        params = {'owner_id': self.id, 'album_id': self.album_id, 'extended': '1', 'photo_sizes': '1', 'rev': '1'}
        print(f'Получаем фото из альбома "{self.album_id}"...', end='')
        try:
            resp = requests.get(self.url, params={**self.params, **params})
            if resp.status_code == 200:
                if not self.get_error_code(resp):
                    return 'Error'
                print('OK')

                albums_counts = resp.json()['response']['count']
                result = []

                for f in resp.json()['response']['items']:
                    for s in f['sizes']:
                        if 'z' in s['type']:
                            result.append({'date': f['date'], 'likes': f['likes']['count'], 'url': s['url']})

                if albums_counts > photo_count_max:
                    result = result[:photo_count_max]

                with open(f'{user_id}_uploads.json', 'w', encoding='utf-8') as f_out:
                    res_out = {}
                    for f in result:
                        file_ext = f['url'].split('?')[0][-3:]
                        date = dt.utcfromtimestamp(f['date']).strftime('%Y%m%d')
                        if f['likes']:
                            # ищем совпадения по имени файла (лайкам) в словаре res_out
                            f_name = str(f['likes'])
                            for file in res_out.values():
                                for fn in file:
                                    if fn['file_name'] == f'{f_name}.{file_ext}':
                                        f_name += f'_{date}'
                        else:
                            f_name = date
                        f_name += f'.{file_ext}'

                        res_out[self.id] = res_out.get(self.id, []) + [
                            {'file_name': f_name, 'url': f['url'], 'size': 'z'}]

                    # создаем каталог пользователя на Я.Диск
                    yd_uploader.make_dir(self.dir_yadisk)
                    # запись файлов фото на ЯД
                    with pbar(len(result), force_tty=True, title='Загрузка') as bar:
                        for el in res_out.values():
                            for f_up in el:
                                bar.title = f"Файл {f_up['file_name']}"
                                yd_uploader.upload_file(f_up['file_name'], f_up['url'], self.dir_yadisk)
                                f_up.pop('url')
                                bar()
                        bar.title = 'Загружено'

                    print('Создаем json файл с загруженными на Я.Диск фото...', end='')
                    json.dump(res_out, f_out, indent=2)
                    print('OK')
                return print('Done !')
            else:
                return print(f"Error {resp.status_code}: {resp.json().get('description')}")
        except requests.ConnectionError or requests.HTTPError:
            return print('\nОшибка подключения к серверу!')


class YaUploader:
    # ссылки на закачку в Я.Диск
    url_mkdir = 'https://cloud-api.yandex.net/v1/disk/resources'
    upload_url = url_mkdir + '/upload'

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Content-Type": "application/json", "Authorization": f"OAuth {self.token}"}

    def make_dir(self, mkdir):
        print(f'Создаем каталог на Я.Диск для user_id {user_id}...', end='')
        resp = requests.get(self.upload_url, params={'path': mkdir}, headers=self.headers)
        if resp.status_code != 201:
            requests.put(self.url_mkdir, params={'path': mkdir}, headers=self.headers)
            print('OK')

    def upload_file(self, filename, url, d_vk):
        """Производит загрузку файла на сервер Я.Диск"""
        try:
            file_path = d_vk + '/' + filename
            # print(f'Загружаем {filename}...', end='\r')
            response = requests.post(self.upload_url, params={'path': file_path, 'url': url}, headers=self.headers)
            if response.status_code == 202:
                # print(f"Файл '{filename}' загружен")
                return
            msg = f"\nОшибка при загрузке файла\nError {response.status_code}: {response.json().get('description')}"
            return msg
        except requests.RequestException:
            return '\nОшибка подключения к серверу'


if __name__ == '__main__':
    user_id = input('Введите id пользователя VK: ')
    album_id = input('Из какого альбома скачивать фото? (wall, profile, saved): ')
    photo_count_max = int(input('Введите количество фото для загрузки на Я.Диск: '))

    # Каталог VK user на Я.Диск
    dir_vk = f'VK/{user_id}'

    # файл с токенами VK и YaD
    with open('tokens') as t:
        vk_token, yd_token = t.read().splitlines()

    vk = VK(vk_token, user_id, album_id, dir_vk)
    yd_uploader = YaUploader(yd_token)

    vk.get_user_info()
    vk.get_user_photo()
