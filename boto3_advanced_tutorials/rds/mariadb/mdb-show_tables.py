import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)

except mdb.Error as e:
    print('Failed to create table'.format(e))
