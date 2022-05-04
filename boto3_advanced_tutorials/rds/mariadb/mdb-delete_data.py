import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    cursor = db.cursor()
    db.autocommit = True
    cursor.execute("DELETE FROM Person WHERE ID=2")
    print(f'{cursor.rowcount} rows deleted')
except mdb.Error as e:
    print('Failed to create table'.format(e))
