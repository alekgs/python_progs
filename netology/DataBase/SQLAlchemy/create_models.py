import sqlalchemy as sq
import sqlalchemy.orm as sqo

Base = sqo.declarative_base()


class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    def __str__(self):
        return self.id


class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    date_sale = sq.Column(sq.DateTime)
    price = sq.Column(sq.Float(precision=2))
    count = sq.Column(sq.Integer)

    stock = sqo.relationship(Stock, backref='sales')

    def __str__(self):
        return self.id


class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), unique=True)

    books = sqo.relationship(Stock, backref='shops')

    def __str__(self):
        return f'Shop name: {self.name}'


class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    title = sq.Column(sq.String(100))

    shops = sqo.relationship(Stock, backref='books')

    def __str__(self):
        return self.title


class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)

    book = sqo.relationship(Book, backref='publishers')

    def __str__(self):
        return self.name


def create_tables(engine, Session):
    with Session() as session:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        session.commit()
        print('Таблицы созданы.')
        print()

