# Design of Form

import tkinter
from tkinter import ttk,messagebox

class Ui:
    
    firstName_Label = None
    firstName_input = None
    contact_label = None
    contact_input = None
    email_label = None
    email_input = None
    gender = None
    gender_male_input = None
    city_label = None
    city_list = None
    role_label = None
    role = None
    tk = None
    
    product_input = None
    price_input = None
    quantity_input = None
    manager_id_input = None

    login_name_input = None
    login_number_input = None
    
    update_id = None
    
    delete_id = None
    delete_item = None  
    
    
    buy_name = None
    buy_quantity = None    
      
    # user/Admin Login form
    def login(self):
        
        lg = tkinter.Tk()
        lg.title('Login')
        lg.geometry('300x300')
        lg.config(bg='lightgray')

        user_label = tkinter.Label(text='Enter User Name ',bg='lightgray',fg='black',font='lucida 10')
        user_label.place(x=100,y=50)
        
        self.login_name_input = tkinter.Entry()
        self.login_name_input.place(x=90,y=80)
        
        login_number_label = tkinter.Label(text='Enter Phone Number',bg='lightgray',fg='black',font='lucida 10')
        login_number_label.place(x=90,y=130)
        
        def login_submit():
            self.login_name_input = self.login_name_input.get()
            self.login_number_input = self.login_number_input.get()
            
            messagebox.showinfo('Welcome','Login Successful')
        
        self.login_number_input = tkinter.Entry()
        self.login_number_input.place(x=90,y=160)

        log_in_btn = tkinter.Button(text='Log in',bg='orange',fg='black',font='Lucida 10',width=10,command = lambda:[login_submit(),lg.destroy()]) 
        log_in_btn.place(x=110,y=230)
        
        lg.mainloop()

    
    # -------------------------------------------------------------------
    
    
    # user/admin Registration form
    def reform(self):
        self.tk = tkinter.Tk()
        self.tk.title('Register Form')
        self.tk.geometry('500x600')
        self.tk.config(bg='lightgray')

        tag = tkinter.Label(text=' Please Enter Details Below ',bg='orange',fg='white',font='Lucida 10 bold',width=63)
        tag.grid(row=0,column=0)

        # Enter Name
        self.firstName_Label = tkinter.Label(text='Name *',bg='lightgray',fg='black',font='Lucida 10') 
        self.firstName_Label.place(x=30,y=40)

        self.firstName_input = tkinter.Entry()
        self.firstName_input.place(x=150,y=43)



        # Enter Contact Number
        self.contact_label = tkinter.Label(text='Contact *',bg='lightgray',fg='black',font='Lucida 10')
        self.contact_label.place(x=30,y=70)


        self.contact_input = tkinter.Entry()
        self.contact_input.place(x=150,y=73)


        # Enter Email Address
        self.email_label = tkinter.Label(text='Email *',bg='lightgray',fg='black',font='Lucida 10') 
        self.email_label.place(x=30,y=100)


        self.email_input = tkinter.Entry()
        self.email_input.place(x=150,y=103)


        # Gender 4
        gender_label = tkinter.Label(text='Gender',bg='lightgray',fg='black',font='Lucida 10')
        gender_label.place(x=30,y=130)


        self.gender_male_input = tkinter.Radiobutton(value=0,text='Male',bg='lightgray',fg='Black',font='Lucida 10')
        self.gender_male_input.place(x=150,y=133)


        gender_female_input = tkinter.Radiobutton(value=1,text='Female',bg='lightgray',fg='black',font='Lucida 10')
        gender_female_input.place(x=250,y=133)


        # city
        self.city_label = tkinter.Label(text='Select Your City',bg='lightgray',fg='black',font='Lucida 10')
        self.city_label.place(x=30,y=160)

        city = ['Rajkot','Ahmadabad','Baroda','Surat','Junagadh','Gandhinagar']
        self.city_list = ttk.Combobox(values=city)
        self.city_list.place(x=150,y=163)

        # role
        self.role_label = tkinter.Label(text='Select Your Role *',bg='lightgray',fg='black',font='Lucida 10')
        self.role_label.place(x=30,y=190)

        role_list = ['Product Manager','Customer']
        self.role = ttk.Combobox(values=role_list)
        self.role.place(x=150,y=193)


        # register button

        def btn_click():

            if(len(self.firstName_input.get()) == 0 ):
                error = tkinter.Label(text='Fill the details where *',bg='lightgray',fg='red',font='Lucida 10')
                error.place(x=190,y=250)

            else:
            
                
                    
                messagebox.showinfo(f'Welcome','Your information has been registered')
                self.firstName_input =  self.firstName_input.get()
                self.contact_input = self.contact_input.get()
                self.email_input = self.email_input.get()
                self.city_list = self.city_list.get() 
                self.role = self.role.get()
                

        reg_btn = tkinter.Button(text='Register',bg='Orange',fg='black',font='Lucida 10',width=20, command=lambda:[btn_click(),self.tk.destroy()] )
        reg_btn.place(x=170,y=300)
        
        login_btn = tkinter.Button(text='Login',bg='Orange',fg='black',font='Lucida 10',width=20,command=lambda:[self.tk.destroy(),self.login()])
        login_btn.place(x=170,y=350)

        self.tk.mainloop()
        
        
    # -------------------------------------------------------------------
        
    # product add form
    def products(self):
        pr = tkinter.Tk()
        pr.title('Add Product')
        pr.geometry('300x200')
        pr.config(bg='lightgray')
        
        
        product_label = tkinter.Label(text='Product Name :',bg='lightgray',fg='black',font='Lucida 10')
        product_label.place(x=25,y=30)
        
        self.product_input = tkinter.Entry()
        self.product_input.place(x=140,y=33) 
        
        price_label = tkinter.Label(text='Product Price :',bg='lightgray',fg='black',font='Lucida 10')
        price_label.place(x=25,y=60)
        
        self.price_input =tkinter.Entry()
        self.price_input.place(x=140,y=63)      
        
        quantity_label = tkinter.Label(text='Product Quantity :',bg='lightgray',fg='black',font='Lucida 10')
        quantity_label.place(x=25,y=90)
        
        self.quantity_input =tkinter.Entry()
        self.quantity_input.place(x=140,y=93)    
        
        # manager_id_label = tkinter.Label(text="Your Id : ",bg='lightgray',fg='black',font='Lucida 10')  
        # manager_id_label.place(x=25,y=120)
        
        # self.manager_id_input = tkinter.Entry()
        # self.manager_id_input.place(x=140,y=123)
        
        
        def add_item():
            
            self.product_input = self.product_input.get()
            self.price_input = self.price_input.get()
            self.quantity_input = self.quantity_input.get()
            # self.manager_id_input = self.manager_id_input.get()
            
            messagebox.showinfo('Welcome','Item has been added') 
            
            
        
        reg_btn = tkinter.Button(text='Add Item',bg='Orange',fg='black',font='Lucida 10',width=15,command = lambda:[
           add_item(),pr.destroy()] )
        reg_btn.place(x=85,y=140)


        pr.mainloop()
    
    
    
    # -------------------------------------------------------------------
    
    
    # update product form
    def update(self):
        up = tkinter.Tk()
        up.title('Update Item')
        up.geometry('300x200')
        up.config(bg='lightgray')
        
        product_label = tkinter.Label(text='Product Name :',bg='lightgray',fg='black',font='Lucida 10')
        product_label.place(x=25,y=30)
        
        self.product_input = tkinter.Entry()
        self.product_input.place(x=140,y=33) 
        
        price_label = tkinter.Label(text='Product Price :',bg='lightgray',fg='black',font='Lucida 10')
        price_label.place(x=25,y=60)
        
        self.price_input =tkinter.Entry()
        self.price_input.place(x=140,y=63)      
        
        quantity_label = tkinter.Label(text='Product Quantity :',bg='lightgray',fg='black',font='Lucida 10')
        quantity_label.place(x=25,y=90)
        
        self.quantity_input =tkinter.Entry()
        self.quantity_input.place(x=140,y=93)    
        
        update_id_label = tkinter.Label(text="Your Id : ",bg='lightgray',fg='black',font='Lucida 10')  
        update_id_label.place(x=25,y=120)
        
        self.update_id = tkinter.Entry()
        self.update_id.place(x=140,y=123)
        
        def update_item():
            
            self.product_input = self.product_input.get()
            self.price_input = self.price_input.get()
            self.quantity_input = self.quantity_input.get()
            self.update_id = self.update_id.get()
            
            messagebox.showinfo('Welcome','Item has been UPDATED') 
            
            
        
        reg_btn = tkinter.Button(text='Update Item',bg='Orange',fg='black',font='Lucida 10',width=15,command = lambda:[
           update_item(),up.destroy()] )
        reg_btn.place(x=85,y=160)
        
        
        up.mainloop()
    

    # -------------------------------------------------------------------
    
    # delete item form
    def delete(self):
        
        dl = tkinter.Tk()
        dl.title('Delete Item')
        dl.geometry('250x200')
        dl.config(bg='lightgray')
        
        delete_id_label = tkinter.Label(text='Your Id :',bg='lightgray',fg='black',font='Lucida 10')
        delete_id_label.place(x=20,y=50)
        
        self.delete_id = tkinter.Entry()
        self.delete_id.place(x=100,y=50)
        
        delete_item_label = tkinter.Label(text='Item Name :',bg='lightgray',fg='black',font='Lucida 10')
        delete_item_label.place(x=20, y=80)
        
        self.delete_item = tkinter.Entry()
        self.delete_item.place(x=100,y=80)
        
        def confirm():
            self.delete_id = self.delete_id.get()
            self.delete_item = self.delete_item.get()

            messagebox.showinfo('warning','Item Has Been Deleted')
        
        del_button = tkinter.Button(text='Delete',bg='orange',fg='black',font='Lucida 10',width=10,command = lambda:[confirm(),dl.destroy()])
        del_button.place(x=80,y=140)

        dl.mainloop()
        
        
    # -------------------------------------------------------------------
    
    
    def buy(self):
        
        by = tkinter.Tk()
        by.title('Shop')
        by.geometry('300x400')
        by.config(bg='lightgray')
        
        buy_name_label = tkinter.Label(text='Item Name :',bg='lightgray',fg='black',font='Lucida 10')
        buy_name_label.place(x=30,y=30)         
        self.buy_name = tkinter.Entry()       
        self.buy_name.place(x=130,y=33)
        
        buy_quantity_label = tkinter.Label(text='Quantity :',bg='lightgray',fg='black',font='Lucida 10')
        buy_quantity_label.place(x=30,y=60) 
        self.buy_quantity = tkinter.Entry()
        self.buy_quantity.place(x=130,y=63)
        
        def buy_btn():
            
            self.buy_name = self.buy_name.get()
            self.buy_quantity = self.buy_quantity.get()
            
            messagebox.showinfo('welcome','Order has been placed')
            
        order_btn = tkinter.Button(text='Order',bg='orange',fg='black',command=lambda:[buy_btn(),by.destroy()],width=15)
        order_btn.place(x=90,y=100) 
        
        by.mainloop()

    
call = Ui()
