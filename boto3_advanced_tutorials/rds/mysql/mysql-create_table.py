import mysql.connector as mc

try: 
    db = mc.connect(
            host='blainedb.cjyewizfkv8j.eu-west-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='dbblaine'
        )
    print('connected')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255))')
    print('Table is created succesfully')
except mc.Error as e:
    print('Failed to create table'.format(e))
