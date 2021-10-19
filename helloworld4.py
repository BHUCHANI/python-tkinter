from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")
    
    print(f"{naamvalue.get(), phonevalue.get(), gendervalue.get(),emergencyvalue.get(),paisanikalvalue.get(), foodservicevalue.get()} ")

    

    with open("records.txt", "a") as f:
        f.write(f"{naamvalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paisanikalvalue.get(), foodservicevalue.get()}\n ")


                   



root.geometry("500x400")

root.title("gadi selmon bhoi chalayega")
Label(root, text="Welcome to Gum hoja travels", font="comicsansns 14 bold").grid(row=0, column=3)
naam = Label(root, text="naam")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency contact")
paisanikal = Label(root, text="paisa nikal")


naamvalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paisanikalvalue = StringVar()
foodservicevalue = IntVar()

naamentry = Entry(root, textvariable=naamvalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paisanikalentry = Entry(root, textvariable=paisanikalvalue)

naamentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paisanikalentry.grid(row=5, column=3)

foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

Button(text="Submit kar nai to", command=getvals).grid(row=7, column=3)

root.mainloop()