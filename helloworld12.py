from tkinter import *
import tkinter.messagebox as tmsg

root =Tk()
root.geometry("450x230")
root.title("ratio button")

def order():
    
    tmsg.showinfo("Amount credited!", f"we have recieved your order for {var.get()} thanks for your order :)")


#var = IntVar
var = StringVar()
var.set("Radio")
#TODO var.set(1) optional
Label(root, text = "Apka menu sir",font="lucida 19 bold", justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="butter chicken", padx=14, variable=var, value="butter chicken").pack()
radio = Radiobutton(root, text="dal makhni", padx=14, variable=var, value="dal makhni").pack()
radio = Radiobutton(root, text="shahi paneer", padx=14, variable=var, value="shahi paneer").pack()
radio = Radiobutton(root, text="rajma chawal", padx=14, variable=var, value="rajma chawal").pack()

Button(text="order now", command=order).pack()
root.mainloop()