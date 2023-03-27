import psycopg2 as psc

DB = 'clients_db'
USER = 'postgres'
PASSWORD = ''


def create_db(conn):
    with conn.cursor() as cursor:
        print(f'Создание отношений в БД {DB}...', end='')
        cursor.execute("""
                 CREATE TABLE IF NOT EXISTS clients
                  (
                    client_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL
                  );
            
                 CREATE TABLE IF NOT EXISTS phones
                  (
                    phone_id SERIAL PRIMARY KEY,
                    client_id INTEGER REFERENCES clients (client_id) ON DELETE CASCADE,
                    phone_number VARCHAR(30) NOT NULL
                  );
                
                 """)
        conn.commit()
        print('OK')


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cursor:
        print(f'Проверяем наличие клиента {first_name} {last_name}'
              f' и email {email} в таблице clients...')

        if find_client(conn, first_name=first_name, last_name=last_name, mode=0) or \
                find_client(conn, email=email, mode=0):
            print('Клиент c данным именем или email уже есть в таблице clients!')
        else:
            print(f'Добавление записи в таблицу clients...', end='')
            cursor.execute("""
                            INSERT INTO
                                   clients (first_name, last_name, email)
                                   VALUES (%s, %s, %s) RETURNING client_id; 
                            """,
                           (first_name, last_name, email))
            client_id = cursor.fetchone()[0]
            print(f'OK (client_id: {client_id})')

            if phone:
                add_phone(conn, client_id, phone)


def add_phone(conn, client_id, phone):
    with conn.cursor() as cursor:
        print(f'Проверяем наличие телефона {phone} у клиента id: {client_id} в таблице phones...')

        if find_client(conn, phone=phone, mode=0):
            print('Такая запись уже есть в таблице phones!')
        else:
            print(f'Добавление записи в таблицу phones...', end='')
            cursor.execute("""
                               INSERT INTO
                               phones (client_id, phone_number)
                               VALUES (%s, %s) 
                               RETURNING phone_id; 
                               """, (client_id, phone))
            print(f'OK (phone_id: {cursor.fetchone()[0]})')


def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cursor:
        print(f'Изменение данных о клиенте client_id: {client_id}...', end='')
        if first_name:
            cursor.execute("""
                               UPDATE clients 
                               SET first_name = %s
                               WHERE client_id = %s; 
                            """, (first_name, client_id))
        if last_name:
            cursor.execute("""
                               UPDATE clients 
                               SET last_name = %s
                               WHERE client_id = %s; 
                           """, (last_name, client_id))
        if email:
            cursor.execute("""
                               UPDATE clients 
                               SET email = %s
                               WHERE client_id = %s;
                           """, (email, client_id))
        conn.commit()
        print('OK')


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cursor:
        print(f'Удаление номера телефона {phone} ...', end='')
        cursor.execute("""
                          DELETE FROM phones WHERE client_id = %s AND phone_number = %s; 
                       """, (client_id, phone))
        conn.commit()
        print('OK')


def delete_client(conn, client_id):
    with conn.cursor() as cursor:
        print(f'Удаление сведений о клиенте client_id: {client_id}... ', end='')
        cursor.execute("""DELETE FROM clients WHERE client_id = %s;""", (client_id,))
        conn.commit()
        print('OK')


def find_client(conn, first_name=None, last_name=None, email=None, phone=None, mode=1):
    """
    Функция осуществляет поиск информации в БД
    mode: mode=0 - не выводит результаты запроса (сделано для функций add_client, add_phone)
          mode=1 - выводит результаты запроса (обычный режим)
    """
    with conn.cursor() as cursor:
        keys = ('first_name', 'last_name', 'email', 'phone_number')
        values = (first_name, last_name, email, phone)
        search_data = {k: v for k, v in zip(keys, values) if v}

        if search_data:
            query_string = ''
            for k, v in search_data.items():
                query_string += f"{k} LIKE %s AND "

            query = """
                       SELECT 
                             first_name,
                             last_name,
                             email,
                             phone_number
                        FROM clients
                             LEFT JOIN phones USING (client_id)   
                        WHERE """

            cursor.execute(query + query_string[:-4], tuple(search_data.values()))
            result = cursor.fetchall()

            if mode:
                print(f'Найдено: {len(result)}')
                if result:
                    [print(s) for s in result]
            else:
                if result:
                    print('Запись не добавлена')
                    return True
                return False
        else:
            print('Нет данных для поиска')


with psc.connect(database=DB, user=USER, password=PASSWORD) as conn:
    # create_db(conn)
    #
    # add_client(conn, 'Lisa', 'Williams', 'harveytimothy@example.org', '(675)990-4919')
    # add_client(conn, 'Brian', 'Jordan', 'christianhoward@example.org', '+1-022-009-5347x996')
    # add_client(conn, 'Alyssa', 'Sanders', 'mcculloughdevin@example.net', '+1-346-203-7363')
    # add_client(conn, 'Diana', 'Stevens', 'brooksbarbara@example.com', '(571)220-9006')
    # add_client(conn, 'Casey', 'Berg', 'yhiggins@example.net', '+1-295-643-2734')
    # add_client(conn, 'Dana', 'Solomon', 'kingshelia@example.com', '+1-798-005-0610')
    # add_client(conn, 'Tyler', 'Watson', 'lindsey25@example.org')
    #
    add_phone(conn, 6, '(129)111-1063')
    # add_phone(conn, 2, '(399)545-5029')
    # add_phone(conn, 3, '(201)333-3252')
    # add_phone(conn, 1, '(675)325-9999')
    # #
    # delete_phone(conn, 9, '(338)409-3865')
    #
    # delete_client(conn, 8)
    #
    # change_client(conn, 3, first_name='Alice', last_name='Johnson', email='alice_johnson@example.net')
    #
    # find_client(conn)
    # find_client(conn, first_name='Casey')
    # find_client(conn, first_name='John')
    # find_client(conn, first_name='Lisa')
    # find_client(conn, first_name='Alyssa')
    # find_client(conn, last_name='Williams')
    # find_client(conn, email='christianhoward@example.org')
    # find_client(conn, phone='+1-798-005-0610')
    # find_client(conn, phone='(675)990-4919')
    # find_client(conn, first_name='Lisa', last_name='Williams')
    # find_client(conn, first_name='Lisa', email='harveytimothy@example.org')
    # find_client(conn, first_name='Lisa', phone='(675)990-4919')
    # find_client(conn, last_name='Williams', email='harveytimothy@example.org', phone='(675)990-4919')
    # find_client(conn, last_name='Williams', phone='(675)990-4919')
    # find_client(conn, email='harveytimothy@example.org', phone='(675)990-4919')
    # find_client(conn, first_name='Lisa', last_name='Williams', email='harveytimothy@example.org', phone='(675)990-4919')



