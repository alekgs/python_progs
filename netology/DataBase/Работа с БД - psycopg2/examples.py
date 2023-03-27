import psycopg2 as ps


def get_collection(cursor, name):
    cursor.execute("""
    SELECT
        DISTINCT collection_name AS Название_сборника,
        artist_name AS Исполнитель
    FROM
        collections
        JOIN track_collections USING(collection_id)
        JOIN tracks USING (track_id)
        JOIN albums USING(album_id)
        JOIN artists_albums USING(album_id)
        JOIN artists USING (artist_id)
    WHERE
        artist_name IN %s;
    """, (name,))
    return cur.fetchall()


def get_count_artist_genre(cursor):
    cursor.execute("""
    SELECT
        genre_name AS Жанр,
        COUNT(DISTINCT artist_name) AS Количество_исполнителей
    FROM
        genres
        JOIN genres_artists USING (genre_id)
        JOIN artists USING (artist_id)
    GROUP BY
        genre_name
    ORDER BY
        genre_name;
    """)
    return cur.fetchall()


conn = ps.connect(database='music_site', user='postgres')

with conn.cursor() as cur:
    # print(get_collection(cur, ('Metallica', 'Rammstein', 'Пилот')))

    for i in get_count_artist_genre(cur):
        print(f'{i[0]}: {i[1]}')

    # conn.commit()

conn.close()
