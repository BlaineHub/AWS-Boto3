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
    query = "DELETE FROM Employee WHERE ID=1"
    cursor.execute(query)
    conn.commit()
    print('{} rows deleted'.format(str(cursor.rowcount)))
except:
    print('Failed...')