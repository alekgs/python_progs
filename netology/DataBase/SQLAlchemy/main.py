from connect_db import connect_db
from create_models import create_tables
from insert_db import insert_data
from search import get_info


def main():
    print('Подключение к БД...', end='')
    engine, session_name = connect_db()
    print('OK\n')

    while True:
        print('Создать таблицы - 1')
        print('Вставка данных  - 2')
        print('Поиск           - 3')
        print('Выход           - 0')

        print()
        command = int(input('Введите команду: '))
        print()

        match command:
            case 1:
                create_tables(engine, session_name)
            case 2:
                insert_data(engine, session_name)
            case 3:
                get_info(engine, session_name)
            case 0:
                exit(0)


if __name__ == '__main__':
    main()
