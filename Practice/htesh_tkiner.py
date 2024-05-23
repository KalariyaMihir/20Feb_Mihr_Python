import tkinter
from tkinter import ttk,messagebox
name : str
file = tkinter.Tk()
file.title('Hitesh')
file.geometry('400x550')
file.config(bg='black')

name_label = tkinter.Label(text='Name : ',bg='black',fg='White',font='Lucida 10 ')
name_label.place(x=30,y=30)

name_input = tkinter.Entry()
name_input.place(x=100,y=30)

def sub():
    name = name_input.get()
    messagebox.showwarning('Warning','Submited')
    print(name)

submit = tkinter.Button(text='Submit',bg='lightgray',fg='blue',font='Lucida 10',command=sub)
submit.place(x=150,y=150)
file.mainloop()


