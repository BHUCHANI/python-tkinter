from tkinter import *
from typing import Sized

def bhuchani(event):
    Sized(f"{event.x}, {event.y}")

root = Tk()
root.title("resizer")
root.geometry("650x350")

widget = Button(root, text='apply')
widget.pack()

widget.bind('<Button-1>', bhuchani)
widget.bind('<Double-1>', quit)

root.mainloop()