import psycopg2

try:
    conn=psycopg2.connect(
        user='postgres',
        password='',
        host='postgresdb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
        port=5432
    )
    conn.autocommit=True
    cursor = conn.cursor()
    query = 'CREATE DATABASE mydb'
    cursor.execute(query)
    print('Database created')
except:
    print('Failed to connect to Database')
