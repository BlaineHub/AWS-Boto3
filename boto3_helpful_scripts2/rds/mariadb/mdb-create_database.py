import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password=''
        )

    dbname = input('Please enter db name: ')
    cursor = db.cursor()
    cursor.execute('CREATE DATABASE {}'.format(dbname))
    print('{} CREATED!'.format(dbname))
except mdb.Error as e:
    print('FAILED!')

