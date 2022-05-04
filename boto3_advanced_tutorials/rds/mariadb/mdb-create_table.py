import mariadb as mdb

try: 
    db = mdb.connect(
            host='mariadb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='mydb'
        )
    print('Connection Created')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255))')
    print('Table is created succesfully')

except mdb.Error as e:
    print('Failed to create table'.format(e))
