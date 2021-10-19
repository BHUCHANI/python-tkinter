from tkinter import *
root = Tk()
root.geometry("730x560")
root.title("Brawl talk")

def myfunc():
    print("kal 8:30 pe brawl talk :Pepe:")

#mymenu = Menu(root)
#mymenu.add_command(label="File", command=myfunc)
#mymenu.add_command(label="Exit", command=quit)
#root.config(menu=mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="new project", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_separator()
m1.add_command(label="save ass", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=yourmenubar)

yourmenubar.add_cascade(label="File", menu=m1)


root.mainloop()