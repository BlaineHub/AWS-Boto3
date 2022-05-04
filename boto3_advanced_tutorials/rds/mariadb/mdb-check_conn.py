import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    print('Connection Created')
except mdb.Error as e:
    print('Connection Failed')
