from Tkinter import *

root = Tk()


label1 = Label( root, text="insignificant ")
E1 = Entry(root, bd =5)


label2 = Label( root, text="low ")
E2 = Entry(root, bd =5)

label3 = Label( root, text=" Moderate")
E3 = Entry(root, bd =5)

label4 = Label( root, text=" High")
E4 = Entry(root, bd =5)


def getDate():
    print E1.get()
    print E2.get()
    print E3.get()
    print E4.get()

submit = Button(root, text ="Submit", command = getDate)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
submit.pack(side =BOTTOM)
root.mainloop()