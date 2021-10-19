from tkinter import *
from typing import Sized

def getvals():
    (uservalue.get())
    (passvalue.get())


root = Tk()
root.title("Thara bhai joginder")
root.geometry("600x400")



user = Label(root, text="naam batao")
password = Label(root, text="password bata jaldi")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="submit kar nai to bawandar ayega", command=getvals).grid()

root.mainloop()