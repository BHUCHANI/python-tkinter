from tkinter import *
from PIL import Image, ImageTk

bhuchani_root = Tk()

bhuchani_root.geometry("500x500")




image = Image.open("download.jpg")
photo = ImageTk.PhotoImage(image)

may_label = Label(image=photo)
may_label.pack()



bhuchani_root.mainloop()