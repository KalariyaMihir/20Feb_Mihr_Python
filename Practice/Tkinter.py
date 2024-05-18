# Tkinter Practice 

import tkinter
from tkinter import ttk,messagebox

tk =  tkinter.Tk()
tk.title("Hello App") #title of app
tk.geometry("500x600") #size of app window
tk.config(bg='gray') 

label_first_name = tkinter.Label(text='First Name :',bg='gray', fg='black',font='Lucida 15 ')
label_first_name.grid(row=0,column=0,sticky='w')

text_first_name = tkinter.Entry()
text_first_name.grid(row=0,column=1,sticky='w')

# ----------------


label_second_name = tkinter.Label(text='Second Name :',bg='gray', fg='black',font='Lucida 15 ')
label_second_name.grid(row=1,column=0,sticky='w')

text_second_name = tkinter.Entry()
text_second_name.grid(row=1,column=1,sticky='w')


# ----------------


label_gender = tkinter.Label(text="Gender    ",bg='gray',fg='black', font='Lucida 15') 
label_gender.grid(row=2,column=0,sticky='w')

gender_male = tkinter.Radiobutton(value=0, text='Male', bg='gray',fg='black',font='Lucida 15')
gender_male.grid(row=2,column=1,sticky='w')

gender_female = tkinter.Radiobutton(value=1,text='Female',bg='Gray', fg='black',font='Lucida 15')
gender_female.grid(row=2,column=2,sticky='w')


# ----------------


language = tkinter.Label(text='Languages',bg='gray',fg='black',font='Lucida 15')
language.grid(row=3,column=0,sticky='w')

choice_1 =  tkinter.Checkbutton(text='     - Gujarati', bg='gray', fg='black',font='Lucida 15')
choice_1.grid(row=4,column=0,sticky='w')

choice_2 = tkinter.Checkbutton(text='     - Hindi',bg='gray',fg='Black',font='Lucida 15')
choice_2.grid(row=5,column=0,sticky='w')

choice_3 = tkinter.Checkbutton(text='     - English',bg='gray',fg='black',font='Lucida 15')
choice_3.grid(row=6,column=0,sticky='w')


# ----------------


city = ['Rajkot','Ahmadabad','Baroda','Surat','Jamnagar']
city_list = ttk.Combobox(values=city)
city_list.grid(row=7,column=0)


# ----------------


# fn_length = text_first_name.get() == None
# sn_length = text_second_name == None

def buttonClick():
    if(len(text_first_name.get()) == 0 ):
        
        messagebox.showerror(f'Error','Enter First Name')
        
    elif(len(text_second_name.get()) == 0):
        messagebox.showerror(f'Error','Enter Second Name')
        
    else:
    
        messagebox.showinfo(f'Welcome',f'{text_first_name.get()} {text_second_name.get()} Your Form has been submitted')

        print(f"First Name : {text_first_name.get()}")
        print(f"Second Name : {text_second_name.get()}")
        
    
btn = tkinter.Button(text='Submit',font='Lucida 15',command=buttonClick)

btn.place(x=250,y=250)


tkinter.mainloop()