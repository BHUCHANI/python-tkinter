from tkinter import *

root = Tk()

canvas_width = 600
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width= canvas_width, height=canvas_height)
can_widget.pack()


can_widget.create_line(0, 0, 800, 400, fill="PINK")
can_widget.create_line(0, 400, 800, 0,fill="BLUE")

can_widget.create_rectangle(6, 9, 500, 400, fill="red")
can_widget.create_text(200, 200, text="bhuchani", fill="yellow")
can_widget.create_oval(400,400,100,100)
root.mainloop()