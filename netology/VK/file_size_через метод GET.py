import requests
url = 'https://sun4-17.userapi.com/impg/46fOyIa3Jjtedxj0w_jHy639yPEyXikFpMKuBg/7FSxuD33VTQ.jpg?size=1224x1224&quality=96&sign=9643d05eb3560dc9435a7c1830bdd299&c_uniq_tag=5GUpKD5splNHyOpImbjrv_zIhLCIbtGjKPxP39C77cQ&type=album'
print('Получаем размер фото из ссылки...', end='')
resp = requests.get(url, stream=True)
if resp.status_code == 200:
    print('OK')
    file_size = resp.headers.get('content-length', 0)
    print('file-size:', file_size, 'byte')
else:
    print('Error:', resp.status_code)
