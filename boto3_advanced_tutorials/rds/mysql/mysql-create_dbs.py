import mysql.connector as mc

try: 
    mydb = mc.connect(
            host='blainedb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password=''
        )

    dbname = input('Please enter db name: ')
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE {}'.format(dbname))
    print(f'{dbname} CREATED!')
except mc.Error as e:
    print('FAILED!')

