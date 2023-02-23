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
        self.shelf = None
        self.name = None
        self.type = None
        self.number = None

    def get_name(self, doc_number):
        """ Принимает номер документа и выводит имя человека, которому он принадлежит
            или сообщение: Документ не найден """
        self.number = doc_number
        res = 'Документ не найден'
        for d_doc in documents:
            if d_doc['number'] == doc_number:
                res = d_doc.get('name', None)
        return res

    def get_directory(self, doc_number):
        """Принимает номер документа и выводит номер полки, на которой он находится
        или сообщение: Полки с таким документом не найдено"""
        self.number = doc_number
        res = 'Полки с таким документом не найдено'
        if self.number:
            for key, value in directories.items():
                if self.number in value:
                    res = key
        return res

    def add(self, type_doc, number, name, shelf):
        """Добавляет новый документ в каталог и в перечень полок"""
        documents.append({'type': type_doc, "number": number, "name": name})
        directories[str(shelf)] = directories.get(str(shelf), []) + [number]


work_with_docs = DocumentsBox()

# тесты
print(work_with_docs.get_name('10006'))
print(work_with_docs.get_name("2207 876234"))
print(work_with_docs.get_name("2207"))

print(work_with_docs.get_directory('11-2'))
print(work_with_docs.get_directory('10006'))

work_with_docs.add('international passport', '311 020203', 'Александр Пушкин', 3)
print(work_with_docs.get_directory('311 020203'))

print(work_with_docs.get_name("311 020203"))
print(work_with_docs.get_directory('311 020204'))

# OK )
