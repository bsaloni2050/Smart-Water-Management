from Tkinter import *
from Tkinter import Tk, Label, BOTH
from PIL import Image, ImageTk


from ttk import Frame, Style

root = Tk()

m1 = PanedWindow(root)
m1.pack(fill=BOTH, expand=1)

opp_name = Label(m1, text="Operator Name :")
opp_value = Label(m1, text=" Saloni")

app_name = Label(m1, text="Application Name :")
app_value = Label(m1, text=" BIocon")

site_name = Label(m1, text="Site Name :")
site_value = Label(m1, text=" Sector 1")

opp_name.pack()
opp_value.pack()
app_name.pack()
app_value.pack()
site_name.pack()
site_value.pack()

Style().configure("TFrame", background="#333")

bard = Image.open("/Users/salonibindra/Desktop/download.jpeg")
bardejov = ImageTk.PhotoImage(bard)
bardejov.pack()

#label1 = Label( image=bardejov)
# label1.image = bardejov
# label1.place(x=20, y=20)
#
# m1.add(opp_name)
# m1.add(opp_value)
# m1.add(app_name)
# m1.add(app_value)
# m1.add(site_name)
# m1.add(site_value)
#
# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)
#
# top = Label(m2, text="top pane")
# m2.add(top)
#
# bottom = Label(m2, text="bottom pane")
# m2.add(bottom)

root.geometry("500x150")
#m1.winfo_geometry(500)
mainloop()