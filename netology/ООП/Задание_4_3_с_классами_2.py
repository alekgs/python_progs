documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '311 020204'],
    '3': []
}


class DocumentsBox:
    def __init__(self):
        self.type = None
        self.number = None
        self.name = None
        self.shelf = None

    def get_name(self):
        """ Принимает номер документа и выводит имя человека, которому он принадлежит
            или сообщение: Документ не найден """
        res = 'Документ не найден'
        for d_doc in documents:
            if d_doc['number'] == self.number:
                res = d_doc.get('name', None)
        return res

    def get_directory(self):
        """Принимает номер документа и выводит номер полки, на которой он находится
        или сообщение: Полки с таким документом не найдено"""
        res = 'Полки с таким документом не найдено'
        if self.number:
            for key, value in directories.items():
                if self.number in value:
                    res = key
        return res

    def add(self):
        """Добавляет новый документ в каталог и в перечень полок"""
        documents.append({'type': self.type, 'number': self.number, 'name': self.name})
        directories[str(self.shelf)] = directories.get(str(self.shelf), []) + [self.number]


work_with_docs = DocumentsBox()

# тесты
work_with_docs.number = '10006'
print(work_with_docs.get_name())

work_with_docs.number = "2207 876234"
print(work_with_docs.get_name())

work_with_docs.number = "2207"
print(work_with_docs.get_name())

work_with_docs.number = '11-2'
print(work_with_docs.get_directory())

work_with_docs.number = '10006'
print(work_with_docs.get_directory())

work_with_docs.type = 'international passport'
work_with_docs.number = '311 020203'
work_with_docs.name = 'Александр Пушкин'
work_with_docs.shelf = 3
work_with_docs.add()

work_with_docs.number = '311 020203'
print(work_with_docs.get_directory())

print(work_with_docs.get_name())

work_with_docs.number = '311 020204'
print(work_with_docs.get_directory())
