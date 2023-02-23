# объявление функции

def convert_to_python_case(text):
    # l = list(text)
    # l1 =  l[1:]
    # for i in range(len(l1)):
    #     if l1[i].isupper():
    #         l1[i] = '_' + l1[i]
    # return (l[0] + ''.join(l1)).lower()
    s = ''
    for el in text:
        if el.isupper():
           s += '_'
        s += el
    return s[1:].lower()

# считываем данные
txt = 'ConvertToInt32YtreKipVnmo76TrekLong'

# вызываем функцию
print(convert_to_python_case(txt))