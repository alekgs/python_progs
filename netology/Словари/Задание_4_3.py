"""
Секретарь
Я работаю секретарем и мне постоянно приходят различные документы.
Я должен быть очень внимателен чтобы не потерять ни один документ.

Каталог документов хранится в следующем виде:
      documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

Перечень полок, на которых находятся документы хранится в следующем виде:
      directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

Необходимо реализовать следующие функции.

get_name — функция, которая принимает номер документа и выводит имя человека,
которому он принадлежит или сообщение: Документ не найден

get_directory — функция, которая принимает номер документа и выводит номер полки,
на которой он находится или сообщение: Полки с таким документом не найдено

add — функция, которая добавляет новый документ в каталог и в перечень полок.

"""

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number: str) -> str or None:
    """ Принимает номер документа и выводит имя человека, которому он принадлежит
    или сообщение: Документ не найден """
    res = 'Документ не найден'
    for d_doc in documents:
        if doc_number in d_doc.get('number'):
            res = d_doc.get('name')
            break
    return res


def get_directory(doc_number: str) -> str or None:
    """Принимает номер документа и выводит номер полки, на которой он находится
    или сообщение: Полки с таким документом не найдено"""
    res = 'Полки с таким документом не найдено'
    if doc_number:
        for key, value in directories.items():
            if doc_number in value:
                res = key
    return res


def add(*args) -> None:
    """Добавляет новый документ в каталог и в перечень полок"""
    if len(args) == 4:
        documents.append({'type': args[0], 'number': args[1], 'name': args[2]})
        directories[str(args[3])] = directories.get(str(args[3]), []) + [args[1]]
    return


# проверка работы реализованных функций
print(get_name("10006"))
print(get_directory("11-2"))
print(get_name("101"))
add('international passport', '311 020203', 'Александр Пушкин', 3)
print(get_directory("311 020203"))
print(get_name("311 020203"))
print(get_directory("311 020204"))
