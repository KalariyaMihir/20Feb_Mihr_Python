# database connectivity page

from RegisterForm import Ui
# import tkinter
import pymysql

v = Ui()

class Tables:
    
    db = None
    cr = None
    v.reform() 
     
    try:
            db = pymysql.connect(host='Localhost',user='root',password='',database='product_management')
            print('Connection Established')
            cr = db.cursor()
    except Exception as e:
            print(e)
            
    # class to create database and tables
    def Database(self) :
    
    
    
        # creating table for customer and manger registration
        try:
                try:
                   tbl_customer = 'create table Customer(id integer primary key auto_increment, Name varchar (30), Contact_No varchar (10), Email varchar(50), gender varchar (7), City varchar (20))'
                   self.cr.execute(tbl_customer) 
                   self.db.commit()  
                
                except Exception as e:
                    print(e) 
                        
                try:
                   tbl_pm = 'create table ProductManager(id integer primary key auto_increment, Name varchar (30), Contact_No varchar (10), Email varchar(50), City varchar (20))'
                   self.cr.execute(tbl_pm) 
                   self.db.commit()
                
                except Exception as e:
                    print(e)
                        
        except Exception as e:
            print(e)
            


        # creating table for customer and manager's  product buying and selling
        if (v.role == 'Product Manager'):

            try :

                items = 'create table items(id integer primary key auto_increment,productName varchar (30), Price int (6), Quantity int (1))'

                self.cr.execute(items)
                self.db.commit()
            
            

            except Exception as e:
                print(e)
                
        elif(v.role == 'Customer'):
            
            try:
                
                buy = 'create table buy(id integer primary key auto_increment,ProductName varchar (30),Quantity int (1))'
                
                self.cr.execute(buy)
                self.db.commit()
            
            except Exception as e:
                print(e)
                
class Manager(Tables):
    
    
    def addItems(self):
        
        try:
            v.products()
            add_item = f"insert into items(productName,Price,Quantity) values('{v.product_input}','{v.price_input}','{v.quantity_input}')"
            
            self.cr.execute(add_item)
            self.db.commit()
           
            
        except Exception as e:
            print(e)
            
    def updateItem(self):
        try :
            v.update()
            update_item = f"Update items set productName = '{v.product_input}',Price = '{v.price_input}',Quantity = '{v.quantity_input}' where id = '{v.update_id}'"
            self.cr.execute(update_item)
            self.db.commit()
            
        except Exception as e:
            print(e) 
               
    def deleteItem(self):
        
        try:
            v.delete_item()
            delete_item = f"delete from items where id = '{v.delete_id}' and productName = '{v.delete_item}'"
            self.cr.execute(delete_item)
            self.db.commit()
            
        except Exception as e:
            print(e)
            


class Customer(Manager):
    
    def showItems(self):
        
        try:
            
            view_item = f"select * from items"
            self.cr.execute(view_item)
            show = self.cr.fetchall()
            
            print('|\tID \t|\t  ITEM \t\t|\t  PRICE \t|\t QUANTITY \t|\n')
            
            for i in show:
                print(f'|\t {i[0]} \t|\t {i[1]} \t|\t {i[2]} \t\t|\t {i[3]} \t\t|')
            
        except Exception as e:
            print(e)

    def buyItems(self):
               
            try:
                self.showItems()
                
                v.buy()
                buy_item = f"insert into buy(ProductName,Quantity)values('{v.buy_name}','{v.buy_quantity}')"

                view_item = f"select * from items"
                self.cr.execute(view_item)
                show = self.cr.fetchall()
                
                for i in show:

                    if v.buy_name in i[1]:
                        
                        update = f"update items set quantity = '{(i[-1]-1)}' where ProductName = '{v.buy_name}'"
                        self.cr.execute(update)
                        self.db.commit()
                        
                self.cr.execute(buy_item)
                self.db.commit()
                
            except Exception as e:
                print(e)
        
tb =  Customer()
tb.Database()

if(v.role == 'Product Manager'):
    
    try:
        
        p_info = f"insert into ProductManager(Name,Contact_No,Email,City) values('{v.firstName_input}','{int(v.contact_input)}','{v.email_input}','{v.city_list}')"

        tb.cr.execute(p_info)
        tb.db.commit()
        
    except Exception as e:
        print(e)
        
elif(v.role == 'Customer'):

    try:
        c_info = f"insert into Customer(Name,Contact_No,Email,City) values('{v.firstName_input}','{v.contact_input}','{v.email_input}','{v.city_list}')"
        
        tb.cr.execute(c_info)
        tb.db.commit()
        
    except Exception as e:
        print(e) 
        
        
def LOGIN():
    view_manager = "select * from ProductManager"
    tb.cr.execute(view_manager)
    show_manager = tb.cr.fetchall() 
    
    for i in show_manager:
    
        if (v.login_name_input == i[1] and v.login_number_input == i[2]):
            
            p_c = 'y'
            
            while p_c == 'y' or p_c == 'Y':
            
                print("""
                      - Press 1 : Add Item 
                      - Press 2 : Update Item
                      - Press 3 : Remove Item
                      """)
                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    tb.addItems()
                if choice == 2:
                    tb.updateItem()
                if choice == 3:
                    tb.deleteItem()
                    
                p_c = input('Want to Perform more operation (y/n)? : ')
            
        else:
            print("Admin Name or Number is Wrong")
                
    view_customer = "select * from Customer"
    tb.cr.execute(view_customer)
    show_customer = tb.cr.fetchall()

    for i in show_customer:
        
        if(v.login_name_input == i[1] and v.login_number_input == i[2]):
            
            c_c = 'y'
            while c_c == 'y' or c_c == 'Y':
                print("""
                        - Press 1 : Show Item
                        - Press 2 : Buy Item
                      """)

                c_choice = int(input("enter Choice : "))

                if (c_choice == 1):
                    tb.showItems()
                elif(c_choice == 2):
                    tb.buyItems()
                c_c = input('Continue shopping (y/n)? : ')
                
        else:
            print("User Name or Number is Wrong")


LOGIN()
