# task to create an e-comers management system 

import pymysql

s_name : str
p_name : str
price : int
quantity : int

try:
    db = pymysql.connect(host='localhost',user='root',password='',database='practice_python')
    print('Connection Established')
    
except Exception as e:
    print(e)
    
cr = db.cursor()

main_choice = 'y'

while main_choice == 'y' or main_choice == 'Y':
    

    print("""

          Press 1 : For Seller
          Press 2 : For Buyer

          """)

    role = int(input("Enter Your Choice : "))

    # for seller
    if(role == 1):

        try :
            tbl_seller = "create table seller(id integer primary key auto_increment, SellerName varchar(30), Product varchar(30), Price integer(6), Quantity integer)"

            cr.execute(tbl_seller)
            db.commit()

            print("Seller Table has been Created")    

        except Exception as e:
            print(e)


        # Insert Item

        try:
            
            seller_choice_loop = 'y'
            
            while seller_choice_loop == 'y' or seller_choice_loop == 'Y' :

                print("""

                          - Enter Your Choice as a Seller -

                                Press 1 : For Add Item
                                Press 2 : For Update Item
                                Press 3 : For Delete Item

                          """)
                sellerChoice = int(input("What do you want to Perform : "))

                # add item for seller
                if(sellerChoice == 1):

                    s_name = input("Enter Seller Name : ")
                    p_name = input("Enter Product Name : ")
                    price = int(input("Enter Product Price : "))
                    quantity = int(input("Enter Number Products : "))

                    insert_item = f"insert into seller(SellerName,Product,Price,Quantity) values('{s_name}', '{p_name}', '{price}', '{quantity}')"

                    cr.execute(insert_item)
                    db.commit()

                    print('👍🏻 Item Added Successfully ')




                # update item for seller
                elif(sellerChoice == 2):

                    print("""

                        - What Do You Want To Update -  

                            Press 1 : For Change Seller Name
                            Press 2 : For Change Product Name 
                            press 3 : For Change Price of Product
                            Press 4 : For Update Quantity of Product

                          """)
                    update_choice = int(input("Enter Your Choice : "))

                    # for update seller name
                    if(update_choice == 1):

                        try : 
                            u_name = input("Enter New Name : ")
                            id = int(input("Enter Id of Seller : "))
                            update_name = f'update seller set SellerNAme = "{u_name}" where id = "{id}"'

                            cr.execute(update_name)
                            db.commit()

                            print(f"👍🏻 Name has been update to {u_name}")

                        except Exception as e:
                            print(e)

                    # for update product name
                    elif(update_choice == 2):

                        try:
                            u_product = input("Enter New Product Name : ")
                            id = int(input("Enter Id of Seller : "))
                            update_product = f'update seller set Product = "{u_product}" where id = "{id}"'

                            cr.execute(update_product)
                            db.commit()

                            print(f"✅ Product Name has been update to {u_product}")

                        except Exception as e:
                            print(e)

                    # for update product price
                    elif(update_choice == 3):

                        try:
                            u_price = input("Enter New Price : ")
                            id = int(input("Enter Id of Seller : "))
                            update_price = f'update seller set Price = "{u_price}" where id = "{id}"'

                            cr.execute(update_price)
                            db.commit()

                            print(f"✅ Product Price has been changed to {u_price}")

                        except Exception as e:
                            print(e)

                    # for update product quantity 
                    elif(update_choice == 4):

                        try:
                            u_quantity = input("Enter New Stock Number : ")
                            id = int(input("Enter Id of Seller : "))
                            update_quantity = f'update seller set Quantity = "{u_quantity}" where id = "{id}"'

                            cr.execute(update_quantity)
                            db.commit()

                            print(f"✅ Product Quantity has been Updated to {u_quantity}")

                        except Exception as e:
                            print(e)




                # for delete an item
                elif(sellerChoice == 3):
                
                    try: 
                        d_product = input("Enter Name of Product : ") 
                        d_id = int(input('Enter Id of Seller '))
                        delete_product = f"delete from Seller where id ='{d_id}' and Product = '{d_product}'"
    
                        cr.execute(delete_product)
                        db.commit()
    
                        print(f"✅ Product Has been Dumped in to 🗑️")
    
                    except Exception as e:
                        print(e)

        except Exception as e:
            print(e)

    elif(role == 2):

        try:

            tbl_buyer = "create table buyer(id integer primary key auto_increment, CostumerName varchar(30), ProductName varchar(30), Item integer, TotalPrice integer)" 
            cr.execute(tbl_buyer)
            db.commit()

            print("Buyer Table has been created")

        except Exception as e:
            print(e)







        buyer_loop_choice = 'y'

        while buyer_loop_choice =='y' or buyer_loop_choice == 'Y':

        
            # buy item 
            print("""
                  What do you want to do : 

                    Press 1 : For View Items
                    Press 2 : For Buy Items

                  """)
            user_choice = int(input("Enter Your Choice : "))


            if (user_choice == 1):

                try : 

                    view_items = 'select * from seller'

                    cr.execute(view_items)
                    show = cr.fetchall()

                    print("------------------------------------------------------------------------")

                    for i in show:

                            print(i)

                    print("\n------------------------------------------------------------------------")


                except Exception as e:
                    print(e)

            elif(user_choice == 2):


                try : 

                    view_items = 'select * from seller'

                    cr.execute(view_items)
                    show = cr.fetchall()

                    print("------------------------------------------------------------------------")

                    for i in show:
                        print(list(i))

                    print("------------------------------------------------------------------------")

                    costumer_name = input("Enter Your Name : ")
                    buy_product_name = input("Enter Product Name : ")
                    buy_quantity = int(input("Enter Quantity : "))


                    for i in show:

                            if (buy_product_name == i[2] and buy_quantity <= i[-1]):
                            
                            
                                total = i[3] * buy_quantity           
                                cart = f"insert into buyer(CostumerName,ProductName,Item,TotalPrice) values('{costumer_name}','{buy_product_name}',{buy_quantity},{total})"
                                cr.execute(cart)
                                db.commit()


                                quantity = i[-1] - buy_quantity

                                minus_item = f"update seller set Quantity = '{quantity}' where Product = '{i[2]}'"
                                cr.execute(minus_item)
                                db.commit()

                                print("👍🏻 Order has been placed ")


                except Exception as e:
                    print(e)
            buyer_loop_choice = input("Continue Shopping (y/n)? : ")

    else:
        print("!OOPS... Invalid Choice")
        
    main_choice = input("Want To change Your Role (y/n) ? : ")