from Tkinter import *

root = Tk()


label1 = Label( root, text="From Date  MM/DD/YYY")
E1 = Entry(root, bd=5)

label2 = Label( root, text="To Date MM/DD/YYY")
E2 = Entry(root, bd=5)


def getDate():
    print E1.get()
    print E2.get()

submit = Button(root, text="Submit", command=getDate)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side=BOTTOM)
root.mainloop()
