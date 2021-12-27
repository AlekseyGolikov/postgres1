import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    with psycopg2.connect(user='user', password='12345', host='localhost', port='5432', database='test') as connection:
        pass
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with connection.cursor() as cursor:
            cursor.execute('SELECT version();')
            record = cursor.fetchone()
            print(f'Connection is established with {record}')

except (Exception, Error) as error:
    print(f'ERROR during PostgreSQL transaction {error}')
finally:
    print('Connection is closed')