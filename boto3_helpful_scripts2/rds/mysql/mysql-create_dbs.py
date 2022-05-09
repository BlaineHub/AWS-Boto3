import mysql.connector as mc

try: 
    mydb = mc.connect(
            host='blogdb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='12345678'
        )

    dbname = input('Please enter db name: ')
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE {}'.format(dbname))
    print(f'{dbname} CREATED!')
except mc.Error as e:
    print('FAILED!')

