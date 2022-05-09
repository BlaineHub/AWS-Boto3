import mysql.connector as mc

try: 
    mydb = mc.connect(
            host='blogdb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password='12345678'
        )
    print('Connection Created')
except mc.Error as e:
    print('Connection Failed')
