# Practice of mysql database

import pymysql

try:
    db = pymysql.connect(host='localhost',user='root',password='',database='python_practice_db')
    print('Connection Established')

except Exception as e:
    print(e)
    
cr = db.cursor()
    
# create table

crt_table = 'create table Student(num integer primary key autoincrement,name varchar(25),city varchar(10))'

try:
    cr.execute(crt_table)
    print('Table Created')

except Exception as e:
    print(e)
    