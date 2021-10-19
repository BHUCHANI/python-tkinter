from tkinter import *

def hello() :
    print("nachoooooooooo")

def name():
    print("naam to suna hi hoga")

root = Tk()
root.geometry("700x300")

frame = Frame(root, borderwidth=6, bg="blue", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 =Button(frame, fg="purple", text="and mand ka tola jo na nacha......", command=hello)
b1.pack(side=LEFT, padx=20)

b2 =Button(frame, fg="purple", text="and mand ka tola jo na nacha......", command=name)
b2.pack(side=LEFT, padx=20)


root.mainloop()