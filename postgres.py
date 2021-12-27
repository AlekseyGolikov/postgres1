import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    with psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', database='test') as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with connection.cursor() as cursor:
            insert_query = """INSERT INTO books (nick_name,author,num_lists,year) VALUES ('aaa','bbb',100,2021);"""
            cursor.execute(insert_query)
            connection.commit()
            print('Note is done successfully!')

            select_query = """SELECT * FROM books;"""
            cursor.execute(select_query)
            result = cursor.fetchall()
            print(f'Result = {result}')

            print()

except (Exception, Error) as error:
    print(f'ERROR during PostgreSQL transaction {error}')
finally:
    print('Connection is closed')