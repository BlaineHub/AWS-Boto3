import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    cursor = db.cursor()
    query = "INSERT INTO Person (name, lastname) VALUES (%s,%s)"
    value = 'Bob','ODriscoll'
    cursor.execute(query,value)
    db.commit()
    print('{} rows inserted'.format(cursor.rowcount))

except mdb.Error as e:
    print('Failed to create table'.format(e))
