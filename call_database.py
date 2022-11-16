import psycopg2

def Connect():
    connection = psycopg2.connect(
        host='localhost',
        database='soluvv_1',
        user='postgres',
        password='9865197446',
        port='5432'
    )
    cur = connection.cursor()
    return cur
