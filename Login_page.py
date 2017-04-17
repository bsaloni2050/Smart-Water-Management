from Tkinter import *
import tkMessageBox

#import Flow_control
import os

root = Tk()


label1 = Label(root, text="User Name")
E1 = Entry(root, bd=5)

label2 = Label(root, text="Password")
E2 = Entry(root, show="*", bd=5)


def getDate():
    if E1.get() == "saloni" and E2.get() == "saloni":
        os.system('python Flow_control.py')
    else:
        tkMessageBox.showerror("Invalid Credentials", "incorrect username & password combination")

submit = Button(root, text="Submit", command=getDate)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side=BOTTOM)
root.title("Welcome to Smart Water Management")
root.geometry("500x150")
root.mainloop()

