"""
В вашем распоряжении имеется файл lorem.txt. Ваша задача посчитать сколько раз встретилось каждое слово в этом тексте. 
Для этого создайте словарь words, где ключом будет слово, а значением - количество раз появления этого слова в тексте.
Регистр букв в словах учитывать не нужно, поэтому слова Hello и hEllO являются эквивалентными.
Значения ключа в словаре words записывайте в верхнем регистре

Например, если перед вами был бы такой текст:

Привет как дела
привет хорошо

то словарь words выглядел бы так

{'ПРИВЕТ': 2, 'КАК': 1, 'ДЕЛА': 1, 'ХОРОШО': 1}

Между словами в файле стоят только пробелы и переносы строк, других разделителей нет. 
Ваша задача только создать переменную-словарь words и подсчитать в нем количество повторений слов. 

"""
with open('lorem.txt', encoding='utf-8') as f:
    words = {}
    for w in f.read().upper().split():
        words[w] = words.get(w, 0) + 1
print(words)
