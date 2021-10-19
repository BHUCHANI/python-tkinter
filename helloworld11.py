from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("450x230")
root.title("Cooler scrollbar")
def getmoni():
    print(f"hamne {myslider2.get()} rupees apke account me bhijwa diye he")
    tmsg.showinfo("Amount credited!", f"hamne {myslider2.get()} rupees apke account me bhijwa diye he")

#myslider = Scale(root, from_=0, to=100)
#myslider.pack()
Label(root,text="kitna rupiya chahiye?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(69)
myslider2.pack()


Button(root, text="hoja mala maal", command=getmoni).pack()

root.mainloop()