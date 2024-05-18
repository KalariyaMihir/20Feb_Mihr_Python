# Design of Form

import tkinter
from tkinter import ttk,messagebox

tk = tkinter.Tk()
tk.title('Register Form')
tk.geometry('500x600')
tk.config(bg='lightgray')

tag = tkinter.Label(text=' Please Enter Details Below ',bg='orange',fg='white',font='Lucida 10 bold',width=63)
tag.grid(row=0,column=0)

# Enter Name
firstName_Label = tkinter.Label(text='Name *',bg='lightgray',fg='black',font='Lucida 10') 
firstName_Label.place(x=30,y=40)

firstName_input = tkinter.Entry()
firstName_input.place(x=150,y=43)



# Enter Contact Number
contact_label = tkinter.Label(text='Contact *',bg='lightgray',fg='black',font='Lucida 10')
contact_label.place(x=30,y=70)


contact_input = tkinter.Entry()
contact_input.place(x=150,y=73)


# Enter Email Address
email_label = tkinter.Label(text='Email *',bg='lightgray',fg='black',font='Lucida 10') 
email_label.place(x=30,y=100)


email_input = tkinter.Entry()
email_input.place(x=150,y=103)


# Gender 4
gender_label = tkinter.Label(text='Gender',bg='lightgray',fg='black',font='Lucida 10')
gender_label.place(x=30,y=130)


gender_male_input = tkinter.Radiobutton(value=0,text='Male',bg='lightgray',fg='Black',font='Lucida 10')
gender_male_input.place(x=150,y=133)


gender_female_input = tkinter.Radiobutton(value=1,text='Female',bg='lightgray',fg='black',font='Lucida 10')
gender_female_input.place(x=250,y=133)


# city
city_label = tkinter.Label(text='Select Your City',bg='lightgray',fg='black',font='Lucida 10')
city_label.place(x=30,y=160)

city = ['Rajkot','Ahmadabad','Baroda','Surat','Junagadh','Gandhinagar']
city_list = ttk.Combobox(values=city)
city_list.place(x=150,y=163)

# role
role_label = tkinter.Label(text='Select Your Role *',bg='lightgray',fg='black',font='Lucida 10')
role_label.place(x=30,y=190)

role = ['Product Manager','Customer']
role = ttk.Combobox(values=role)
role.place(x=150,y=193)


tk.mainloop()
