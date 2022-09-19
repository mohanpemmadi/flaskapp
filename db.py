import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='company',
                            user='postgres',
                            password='root',
                            port='5432')

    return conn