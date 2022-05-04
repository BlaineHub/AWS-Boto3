import mysql.connector as mc

try: 
    dbname = input('Please enter the database name: ')
    tablename = input('Please eneter the table name: ')
    db = mc.connect(
            host='blainedb.cjyewizfkv8j.eu-west-1.rds.amazonaws.com',
            user='admin',
            password='',
            database=dbname
        )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM {}".format(tablename))
    result = cursor.fetchall()

    for data in result:
        print(data)
    

except mc.Error as e:
    print('Error: {}'.format(e))