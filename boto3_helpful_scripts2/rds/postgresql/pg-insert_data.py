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

    query = "INSERT INTO Employee (ID, NAME, EMAIL) VALUES (2,%s,%s)"
    values='Bob','Bob@gmail.com'
    cursor.execute(query,values)
    conn.commit()
    print('Success...')
except:
    print('Failed...')
