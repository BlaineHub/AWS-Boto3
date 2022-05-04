import mysql.connector as mc

try: 
    mydb = mc.connect(
            host='blainedb.cmugpmb5tbfm.us-east-1.rds.amazonaws.com',
            user='admin',
            password=''
        )
    print('Connection Created')
except mc.Error as e:
    print('Connection Failed')
