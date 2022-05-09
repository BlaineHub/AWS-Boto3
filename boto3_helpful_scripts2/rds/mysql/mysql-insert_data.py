import mysql.connector as mc

try: 
    db = mc.connect(
            host='blainedb.cjyewizfkv8j.eu-west-1.rds.amazonaws.com',
            user='admin',
            password='',
            database='dbblaine'
        )
    cursor = db.cursor()
    name = input('Please enter your name: ')
    lastname = input('plese eneter your last name: ')
    query = "INSERT INTO Person (name, lastname) VALUES (%s,%s)"
    value = name,lastname
    cursor.execute(query,value)
    db.commit()
    print('Data Inserted')

except mc.Error as e:
    print('Error: {}'.format(e))