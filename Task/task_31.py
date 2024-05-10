# create db dynamic

import sqlite3,os

os.chdir('Task')
db = sqlite3.connect('ST_Db.db')

# create table

crt_table = 'create table Student(num integer primary key autoincrement,name varchar(25),city varchar(10))'

try:
    db.execute(crt_table)
    print('Table Created')

except Exception as e:
    print(e)
    
    
    
# insert data

choice = input("Want to Add Student ? (y/n) : ")

while choice == 'y' or choice == 'Y':
    name = input("Enter Name : ")
    city = input("Enter City : ")
    
    insert_data = f"insert into Student(name , city) values('{name}','{city}')"

    try:
        db.execute(insert_data)
        db.commit()
        print('Student Registered')

    except Exception as e:
        print(e)

    choice = input("Add More Student ? (y/n) : ")
    


# See Data
cr = db.cursor()

see = 'select name from Student '

try:
    cr.execute(see)
    data = cr.fetchmany()
    print(data)
    
except Exception as f:
    print(f)
