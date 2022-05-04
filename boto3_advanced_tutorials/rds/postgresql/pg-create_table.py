import psycopg2

try:
    conn=psycopg2.connect(
        database='mydb',
        user='postgres',
        password='',
        host='postgresdb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
        port=5432
    )
    cursor = conn.cursor()
    query = 'CREATE TABLE Employee (ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL, EMAIL TEXT NOT NULL)'
    cursor.execute(query)
    conn.commit()
    print('Success....')
except:
    print('Failed...')
