from tkinter import *
window = Tk()

window.geometry("580x250")
window.title("Midterm in OOP")

fullname = StringVar()
def bttn():
    name = fullname.get()
    txtfld2.delete(0, END)
    txtfld2.insert(0, name)

lbl = Label(window, text="Enter your fullname:", fg="red")
lbl.place(x=40, y=80)

txtfld1 = Entry(window, textvariable = fullname  , bd=5, font=("calibre", 16))
txtfld1.place(x=280, y=80)

btn = Button(window, text="Click to display your Fullname", fg="red", command = bttn)
btn.place(x=40, y=130)

txtfld2 = Entry(window, bd=5, font=("calibre", 16))
txtfld2.place(x=280, y=130)

window.mainloop()
