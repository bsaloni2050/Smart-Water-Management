from Tkinter import *
import csv, sqlite3
from tabulate import tabulate

import pandas
root = Tk()
root.geometry("900x700+200+250")

con = sqlite3.connect("epanet.db")
cur = con.cursor()
tup = []

path = '/Users/salonibindra/Desktop/output1.csv'
df = pandas.read_csv(path)
df.to_sql('epanet', con, if_exists='append', index=False)
# x = cur.execute("Select * from epanet where Node_ID = 'Node J-2'")
cur.execute("Select DISTINCT Node_ID from epanet group by Node_ID")
node_name = list(cur.fetchall())


mb1 = Menubutton(text="Node ID's", relief=RAISED)
mb1.grid(row=5, column=0)
mb1.menu = Menu(mb1, tearoff=0)
mb1["menu"] = mb1.menu
mayoVar = IntVar()
for x in node_name:
    mb1.menu.add_checkbutton(label=x, variable=mayoVar )#command=self.uploadEpanetData('node'))

mb = Menubutton(text="Node ID's", relief=RAISED)
mb.grid(row=2, column=0)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mayoVar = IntVar()
mb.menu.add_checkbutton(label="hey", variable=mayoVar )#command=self.uploadEpanetData('node'))


#data = list(cur.fetchall())
con.commit()
con.close()

# columns =['Time',	'Elevation',	'Base Demand',	'Initial_Quality',	'Demand',	'Head',	'Pressure',	'Quality',	'Node_id']
#
# for r in range(25):
#     for i in range(9):
#         l = Label(text=data[r][i], relief=RIDGE)
#         l.grid(row=r+1, column=i, sticky=NSEW)
#
# for d in range(len(columns)):
#     l = Label(text=columns[d], relief=RIDGE)
#     l.grid(row=0, column=d, sticky=NSEW)
#
#
root.mainloop()
