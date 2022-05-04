import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Person")
    for row in cursor:
        print(row)

except mdb.Error as e:
    print('Failed to create table'.format(e))
