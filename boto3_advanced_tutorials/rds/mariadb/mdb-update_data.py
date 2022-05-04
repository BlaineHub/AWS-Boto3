import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    cursor = db.cursor()
    cursor.execute("UPDATE Person SET name='updated' WHERE ID=2")
    db.commit()
    print(f'{cursor.rowcount} rows updated')
except mdb.Error as e:
    print('Failed to create table'.format(e))
