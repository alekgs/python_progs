from faker import Faker
import random as rnd

fake = Faker()
Faker.seed()


def get_genre(count, *args):
    """
     Генератор жанров   
    """
    with open(f'{args[0]}.sql', 'w', encoding='UTF-8') as f_genre:
        f_genre.write(f"INSERT INTO\n  {args[0]} ({', '.join(args[1:])})\nVALUES\n")
        for i in range(1, count + 1):
            f_genre.write(f"   ({i}, '{fake.word().title()}'){(',', ';')[i == count]}\n")


def get_artists(count, *args):
    """
    Генератор имен артистов
    """
    with open(f'{args[0]}.sql', 'w', encoding='UTF-8') as f_art:
        f_art.write(f"INSERT INTO\n  {args[0]} ({', '.join(args[1:])})\nVALUES\n")
        for i in range(1, count + 1):
            names = [fake.first_name(), fake.last_name(), fake.company(), fake.name()]
            f_art.write(f"   ({i}, '{rnd.choice(names)}'){(',', ';')[i == count]}\n")


def get_album(count, *args):
    """
     Генератор альбомов   
    """
    with open(f'{args[0]}.sql', 'w', encoding='UTF-8') as f_album:
        f_album.write(f"INSERT INTO\n  {args[0]} ({', '.join(args[1:])})\nVALUES\n")
        for i in range(1, count + 1):
            f_album.write(f"   ({i}, '{fake.text(max_nb_chars=20)[:-1]}', {rnd.randint(2018, 2023)})")
            f_album.write(f"{(',', ';')[i == count]}\n")


def get_tracks(count, albums_cnt, *args):
    """
     Генератор треков
    """
    with open(f'{args[0]}.sql', 'w', encoding='UTF-8') as f_tracks:
        f_tracks.write(f"INSERT INTO\n  {args[0]} ({', '.join(args[1:])})\nVALUES\n")
        for i in range(1, count - 1):
            f_tracks.write(
                            f"   ({i}, {rnd.randint(1, albums_cnt)}, "
                            f"'{fake.sentence(nb_words=4)[:-1]}', "
                            f"'00:{rnd.randint(0,16):02}:{rnd.randint(0,60):02}'), \n"
                           )
        # Добавим для выполнения условий дом. задания несколько строк со словами "мой, my"
        for i in range(count - 2, count + 1):
            f_tracks.write(
                f"   ({i}, {rnd.randint(1, albums_cnt)}, "
                f"'{fake.sentence(nb_words=4, variable_nb_words=False, ext_word_list= ['my', 'мой', 'Loving', 'track', 'Лучший'])[:-1]}', "
                f"'00:{rnd.randint(0, 16):02}:{rnd.randint(0, 60):02}')"
            )
            f_tracks.write(f"{(',', ';')[i == count + 3]}\n")


def get_collection(count, *args):
    """
     Генератор коллекций
    """
    with open(f'{args[0]}.sql', 'w', encoding='UTF-8') as f_coll:
        f_coll.write(f"INSERT INTO\n  {args[0]} ({', '.join(args[1:])})\nVALUES\n")
        for i in range(1, count + 1):
            year = rnd.randint(2018, 2023)
            f_coll.write(f"   ({i}, '{fake.text(max_nb_chars=30)[:-1]}', {year}){(',', ';')[i == count]}\n")


def main():
    print('Генератор тестовых данных для заполнения БД "Музыкальный сайт"')
    print('Формирует файлы формата sql с командами INSERT')
    print()
    print('Внимание ! Необходимо изменить описание атрибутов под свои таблицы !')

    # !!!! Изменить под свои таблицы !!!!!
    # Описание таблиц [имя_таблицы, атрибут1, ..., атрибутN]
    table_genre = ['genre', 'genre_id', 'genre_name']
    table_artists = ['artists', 'artist_id', 'artist_name']
    table_albums = ['albums', 'album_id', 'album_title', 'album_year']
    table_tracks = ['tracks', 'track_id', 'album_id', 'track_title', 'track_duration']
    table_collections = ['collections', 'collection_id', 'collection_name', 'collection_year']

    genres_count = int(input('Введите кол-во жанров: '))
    artists_count = int(input('Введите кол-во исполнителей: '))
    albums_count = int(input('Введите кол-во альбомов: '))
    collections_count = int(input('Введите кол-во коллекций: '))
    tracks_count = int(input('Введите кол-во треков: '))

    get_genre(genres_count, *table_genre)
    get_artists(artists_count, *table_artists)
    get_album(albums_count, *table_albums)
    get_tracks(tracks_count, albums_count, *table_tracks)
    get_collection(collections_count, *table_collections)


if __name__ == '__main__':
    main()
