from create_models import Publisher, Shop, Book, Stock, Sale
import json


def insert_data(engine, Session):
    with Session() as session:
        with open('fixtures/tests_data.json', encoding='utf-8') as fd:
            data = json.load(fd)
            for record in data:
                model = {
                         'publisher': Publisher,
                         'shop': Shop,
                         'book': Book,
                         'stock': Stock,
                         'sale': Sale}[record.get('model')]
                session.add(model(id=record.get('pk'), **record.get('fields')))
            session.commit()
            print('Данные добавлены.')
            print()
