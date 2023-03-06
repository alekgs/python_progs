"""
Итоговая работа по модулю "Основы языка программирования"
Нужно написать программу, которая будет:
    Получать фотографии с профиля ВК. Для этого нужно использовать метод photos.get.
    Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
    Для имени фотографий использовать количество лайков. Если количество лайков одинаково, то добавить дату загрузки
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

    def __init__(self, token, u_id, dir_yadisk, a_id, version='5.131'):
        self.token = token
        self.id = u_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        self.album_id = a_id
        self.dir_yadisk = dir_yadisk

    @staticmethod
    def get_error_code(rsp):
        """ Метод возвращает ответы ошибок при работе с API ВК"""
        if 'error' in rsp.json().keys():
            err_code = rsp.json()['error']['error_code']
            err_msg = rsp.json()['error']['error_msg']
            print(f'\nОшибка получения данных !\n{err_code}: {err_msg}')
            return False
        return True

    def get_user_info(self):
        """
        Метод получает краткую информацию о пользователе ВК, а также
        преобразует id пользователя в цифровой вид (если был введен screen_name)
        """
        print(f'\nПолучаем информацию по {self.id}...', end='')
        params = {'user_ids': self.id, 'fields': 'screen_name'}
        resp = requests.post(self.url_user_get, params={**self.params, **params})
        if resp.status_code == 200:
            if not self.get_error_code(resp):
                return exit('Error')
            if resp.json()['response']:
                print('OK')
                u_info = resp.json()['response'][0]
                self.id = u_info['id']
                return print(f"id:{u_info['id']} ({u_info['screen_name']}), {u_info['first_name']} {u_info['last_name']}")
            print(f'\nПользователь VK с id {self.id} не найден')
            return exit(0)

    def get_user_photo(self, photo_count_max=5):
        """
        Метод получает json с информацией о фото пользователя ВК
        и возвращает список словарей для формирования ссылок
        на закачку фото на Я.Диск
        """
        params = {'owner_id': self.id, 'album_id': self.album_id, 'extended': '1', 'photo_sizes': '1', 'rev': '1'}
        print(f'Получаем фото из альбома "{self.album_id}"...', end='')
        try:
            resp = requests.get(self.url, params={**self.params, **params})
            if resp.status_code == 200:
                if not self.get_error_code(resp):
                    return exit('Error')
                print('OK')
                albums_count = resp.json()['response']['count']
                result = []
                for f in resp.json()['response']['items']:
                    for s in f['sizes']:
                        if 'z' in s['type']:
                            result.append({'date': f['date'], 'likes': f['likes']['count'], 'url': s['url']})
                if albums_count > photo_count_max:
                    result = result[:photo_count_max]
                return result
            else:
                return print(f"Error {resp.status_code}: {resp.json().get('description')}")
        except requests.ConnectionError or requests.HTTPError:
            return print('\nОшибка подключения к серверу!')

    def get_parsed_photo(self, photo_info: list):
        """
        Метод парсит список json, полученный из get_user_photo.
        Возвращает словарь с именами файлов фото и их ссылками на закачку
        """
        res_out = {}
        for f in photo_info:
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
        return res_out


class YaDisk:
    # ссылки на закачку в Я.Диск
    url_mkdir = 'https://cloud-api.yandex.net/v1/disk/resources'
    upload_url = url_mkdir + '/upload'

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Content-Type": "application/json",
                        "Accept": "application/json",
                        "Authorization": f"OAuth {self.token}"}

    def make_dir(self, mkdir):
        """ Создает каталог на Я.Диске """

        print(f'Создаем каталог {mkdir} на Я.Диск...', end='')
        resp = requests.get(self.upload_url, params={'path': mkdir}, headers=self.headers)
        if resp.status_code != 201:
            requests.put(self.url_mkdir, params={'path': mkdir}, headers=self.headers)
        print('OK')

    def upload_file(self, res_parsed, d_vk, u_id, ph_count):
        """ Производит загрузку файла на сервер Я.Диск """
        with pbar(ph_count, force_tty=True, title='Загрузка', stats=None) as bar:
            for el in res_parsed.values():
                for f in el:
                    bar.title = f"Файл {f['file_name']}"
                    f_path = d_vk + '/' + f['file_name']
                    resp = requests.post(self.upload_url, params={'path': f_path, 'url': f['url']}, headers=self.headers)
                    f.pop('url')
                    if resp.status_code != 202:
                        msg = f"\nОшибка при загрузке файла\nError {resp.status_code}: {resp.json().get('description')}"
                        return print(msg)
                    bar()
            bar.title = 'Done'

        print('Создаем json файл с загруженными на Я.Диск фото...', end='')
        with open(f'{u_id}_uploads.json', 'w', encoding='utf-8') as f_out:
            json.dump(res_parsed, f_out, indent=3)
        print('OK')

        print('Файлы успешно загружены на Я.Диск')
        return


def main():
    user_id = input('Введите id пользователя VK: ')

    album_id = input('Альбом ВК для скачивания фото? (wall, profile, saved) [profile]: ')
    if len(album_id) == 0:
        album_id = 'profile'

    p = input('Количество фото для загрузки на Я.Диск [5]: ')
    if len(p):
        photo_count_max = int(p)
    else:
        photo_count_max = 5

    # Каталог VK user на Я.Диск
    dir_vk = f'VK/{user_id}'
    # dir_vk = f'/{user_id}'

    # файл с токенами VK и YaD
    with open('.tokens') as t:
        vk_token, yd_token = t.read().splitlines()

    vk = VK(vk_token, user_id, dir_vk, album_id)
    yd = YaDisk(yd_token)

    # получаем инфо пользователя, а также приводим
    # id screen_name (если был введен такой) в цифровой вид
    vk.get_user_info()
    # получаем фото профиля из ВК
    res_json = vk.get_user_photo(photo_count_max)
    # парсим полученный результат
    res_parsed_photos = vk.get_parsed_photo(res_json)
    # создаем каталог пользователя на Я.Диск
    yd.make_dir(dir_vk)
    # Загружаем фото пользователя на Я.Диск
    yd.upload_file(res_parsed_photos, dir_vk, user_id, photo_count_max)


if __name__ == '__main__':
    main()
