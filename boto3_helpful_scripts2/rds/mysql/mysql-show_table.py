import mysql.connector as mc

try: 
    db = mc.connect(
            host='blogdb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='12345678',
            database='blogdb'
        )
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')
    #SHOW DATABASES

    for table in cursor:
        print(table)
except mc.Error as e:
    print('Error: {}'.format(e))
