"""
В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
Ключ для декодирования располагается в json-файле. В качестве ответа нужно просто отправить получившийся текст.
И обратите внимание, что раскодировать нужно только лишь буквы, все остальные символы(цифры, знаки пунктуации и т.д.)
необходимо выводить как есть.

"""
import json

with open('Alphabet.json') as f_keys, open('Abracadabra__1_.txt') as f_txt:
    keys = json.load(f_keys)
    text = f_txt.read()
[print(keys.get(w, w), end='') for w in text]


# with open('Alphabet.json') as f:
#     key = json.load(f)
# with open('Abracadabra.txt', encoding='utf-8') as f:
#     txt = f.read()
# print(txt.translate(txt.maketrans(key)))
