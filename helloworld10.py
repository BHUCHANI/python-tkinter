from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("730x560")
root.title("Brawl talk")

def myfunc():
    print("Aaj 8:30 pe brawl talk :Pepe:")

def help():
    print("me tumhari madad karunga balak")
    a = tmsg.showinfo("Help", "Bhuchani tumhari madad karega balak")

def rate():
    print("5 star rating de nai to HACK KARDUGA")
    value = tmsg.askquestion("Chup chap 5 star rating de with smile :)")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what wrong. We will try to improve soon"
    tmsg.showinfo("Experience", msg)

def alexa():
    ans = tmsg.askretrycancel("alexa se dosti karlo", "sorry alexa nahi banegi aki dost")
    if ans:
        print("Retry karo jab tak dost na bane")

    else:
        print("pls try again later")

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="new project", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_separator()
m1.add_command(label="save ass", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="File", menu=m1)

m2 = Menu(yourmenubar, tearoff=0)
m2.add_command(label="cut", command=myfunc)
m2.add_command(label="copy", command=myfunc)
m2.add_separator()
m2.add_command(label="chipka", command=myfunc)
m2.add_command(label="chapde", command=myfunc)
root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="Edit", menu=m2)

m3 = Menu(yourmenubar, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate", command=rate)
m3.add_command(label="Befriendalexa", command=alexa)
yourmenubar.add_cascade(label="Help", menu=m3)
root.config(menu=yourmenubar)
root.mainloop()