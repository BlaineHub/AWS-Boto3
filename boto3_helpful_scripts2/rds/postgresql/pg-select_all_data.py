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
    query = "SELECT * FROM Employee"
    cursor.execute(query)
    rows = cursor.fetchall()
    for data in rows:
        print(data)
except:
    print('Failed...')