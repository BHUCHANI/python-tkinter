from tkinter import *

root = Tk()
root.geometry("500x500")
def resize():

    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")
    
root.title("Doraemon ki big and small light")
Label(text="", pady=10).grid(row=2, column=1)

Label(text="width:").grid(row=1, column=1)
Label(text="height:").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
height_entry = Entry(root, textvariable=height).grid(row=2, column=2)
 
Button(text="Apply", command=resize,pady=2).grid(column=2)

root.mainloop()
