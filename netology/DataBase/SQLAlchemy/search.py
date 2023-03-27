from create_models import Publisher, Shop, Book, Stock, Sale


def get_info(engine, Session):
    name_id = input('Введите имя или id издателя: ')

    with Session() as session:
        query = session.query(Shop)
        query = query.join(Stock, Stock.id_shop == Shop.id)
        query = query.join(Book, Book.id == Stock.id_book)
        query = query.join(Publisher, Publisher.id == Book.id_publisher)

        if name_id.isdigit():
            res = query.filter(Publisher.id == int(name_id))

            query_client = session.query(Publisher)
            res_client = query_client.filter(Publisher.id == int(name_id))
            name_id = f'id {name_id}'
        else:
            res = query.filter(Publisher.name.like(f"%{name_id}%"))

        if res.all():
            print(f'Клиент: {name_id} ({res_client.all()[0]})')
            [print(shop) for shop in res.all()]
        else:
            print(f'Клиент ({name_id}) не найден')
        print()
