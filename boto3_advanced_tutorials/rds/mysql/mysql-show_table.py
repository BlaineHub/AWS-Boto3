import mysql.connector as mc

try: 
    db = mc.connect(
            host='blainedb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='blainedb'
        )
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')

    for table in cursor:
        print(table)
except mc.Error as e:
    print('Error: {}'.format(e))
