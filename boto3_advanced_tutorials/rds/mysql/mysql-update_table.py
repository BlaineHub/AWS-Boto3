import mysql.connector as mc

try: 
    db = mc.connect(
            host='blainedb.cjyewizfkv8j.eu-west-1.rds.amazonaws.com',
            user='admin',
            password='',
            database= 'dbblaine'
        )
    cursor = db.cursor()
    query = "UPDATE Person SET name='updated' WHERE id='4'"
    cursor.execute(query)
    db.commit()
    print(cursor.rowcount, "Records effected")

except mc.Error as e:
    print('Error: {}'.format(e))