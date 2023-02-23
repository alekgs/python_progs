import os
import requests

def download_file(self, url: str, d_img: str):
    resp = requests.get(url, stream=True)
    if resp.status_code == 200:
        file_name = d_img + '/' + url.split('?')[0].split('/')[-1]
        # file_name = f'{int(dt.today().timestamp())}.jpg'
        with open(file_name, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    else:
        print('Ошибка загрузки файла')

# создаем каталог для фото с VK ID
# dir_images = 'id' + id + '_images'
#     if not os.path.isdir(dir_images):
#         os.mkdir(dir_images)

# скачиваем файл на локальный диск
# self.download_file(s['url'], dir_images)