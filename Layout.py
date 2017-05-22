'''This is the Layout using Tkinter'''

from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style
from tkinter import *
import tkMessageBox
import Tkinter
import os
from PIL import ImageTk, Image
import matplotlib as plt
# from matplotlib.use("TkAgg")
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkFileDialog import askopenfilenames
from tkinter import Tk
from tkFileDialog import askopenfilenames
from tkinter import filedialog
import sqlite3, pandas


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Smart Water Management")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        label2 = Label(self, text="Corporation Name: W-Smart")
        label2.grid(row=3, column=0, sticky=W)
        label3 = Label(self, text="Operator Name: Saloni")
        label3.grid(row=4, column=0, sticky=W)
        label4 = Label(self, text="Designation: Consultant")
        label4.grid(row=5, column=0, sticky=W)
        label8 = Label(self, text="Site Name : Lille")
        label8.grid(row=6, column=0, sticky=W)
        # label6 = Label(self, text="Application Name: ")
        # label6.grid(row=6, column=0, sticky=W)

        mb1 = Menubutton(self, text="Application Name  ", relief=RAISED)
        mb1.grid(row=12, column=0, sticky=W)
        mb1.menu = Menu(mb1, tearoff=0)
        mb1["menu"] = mb1.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb1.menu.add_checkbutton(label="BioCon", variable=mayoVar, command=self.epanetMainMenu)
        mb1.menu.add_checkbutton(label="Net Leak", variable=ketchVar)
        mb1.menu.add_checkbutton(label="EnCon", variable=ketchVar)

        mb = Menubutton(self, text="Site Map", relief=RAISED)
        mb.grid(row=8, column=0, sticky=W)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb.menu.add_checkbutton(label="GIS", variable=mayoVar, command=self.launch_GIS)
        mb.menu.add_checkbutton(label="Google Earth", variable=ketchVar, command=self.launch_GoogleEarth)

        # submit = Button(self, text="Launch EPANET", command= self.launch)
        # submit.grid(row=17, column =0, sticky=W)

        bard = Image.open("/Users/salonibindra/Documents/work/Smart-Water-Management/Images/sitemap.png")
        bard1 = bard.resize((550, 650), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard1)
        label1 = Label(self, image=bardejov, borderwidth=2, relief="solid")
        label1.image = bardejov
        label1.grid(row=3, column=2, columnspan=6, rowspan=40, sticky=E + W + S + N, padx=50, pady=15)

    def launch_GIS(self):
        # os.system("open /Applications/Safari.app")
        webbrowser.open("https://www.arcgis.com/home/index.html")
        self.initUI()
        path = self.fileupload()
        bard = Image.open(path)
        bard1 = bard.resize((550, 650), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard1)
        label1 = Label(self, image=bardejov, borderwidth=2, relief="solid")
        label1.image = bardejov
        label1.grid(row=3, column=2, columnspan=6, rowspan=40, sticky=E + W + S + N, padx=50, pady=15)

    def fileupload(self):
        print ('in file upload')
        tk = Tk()
        tk.filename = filedialog.askopenfilename(title="choose your file")
        # ,filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print (tk.filename)
        tk.withdraw()
        return tk.filename.strip("(,',)")

    def launch_GoogleEarth(self):
        webbrowser.open("https://earth.google.com/web/")

        self.initUI()
        path = self.fileupload()
        bard = Image.open(path)
        bard1 = bard.resize((550, 650), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard1)
        label1 = Label(self, image=bardejov, borderwidth=2, relief="solid")
        label1.image = bardejov
        label1.grid(row=3, column=2, columnspan=6, rowspan=40, sticky=E + W + S + N, padx=50, pady=15)

    def epanetMainMenu(self):
        self.initUI()

        self.parent.title("Smart Water Management : BioCon")

        label2 = Label(self, text=" Application Name:  BioCon")
        label2.grid(row=12, column=0, sticky=W)

        submit = Button(self, text="Launch EPANET", command=self.launch_Epanet)
        submit.grid(row=18, column=0, sticky=W)
        print ('launch epanet b4')

        mb = Menubutton(self, text="Data Analysis", relief=RAISED)
        mb.grid(row=14, column=0, sticky=W)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb.menu.add_checkbutton(label="Spot Analysis", variable=mayoVar, command=self.donothing)
        mb.menu.add_checkbutton(label=" DMA", variable=ketchVar)

    def launch_Epanet(self):
        webbrowser.open("http://epanet.de/")
        print ('launching epanet....')
        #
        print ('b4 upload graph')
        #
        # mb = Menubutton(self, text="Upload Data", relief=RAISED)
        # mb.grid(row=20, column=0, sticky=W)
        # mb.menu = Menu(mb, tearoff=0)
        # mb["menu"] = mb.menu
        # mayoVar = IntVar()
        # ketchVar = IntVar()
        # ketchVar1 = IntVar()
        # mb.menu.add_checkbutton(label="Pipe", variable=mayoVar, command=self.uploadEpanetData('pipe'))
        # mb.menu.add_checkbutton(label=" Nodes", variable=ketchVar, command=self.uploadEpanetData('Nodes'))
        # mb.menu.add_checkbutton(label=" Reservoir", variable=ketchVar1, command=self.uploadEpanetData('Reservoir'))

        # submit = Button(self, text="Upload Data", command=self.uploadEpanetData_ChooseType)
        # submit.grid(row=20, column=0, sticky=W)

        submit = Button(self, text="Upload Graph", command=self.uploadEpanetGraph)
        submit.grid(row=19, column=0, sticky=W)
        print ('after upload garph')

        print ('b4 upload data')

        submit = Button(self, text="Upload Data for Pipes", command=self.uploadEpanetDataPipe)
        submit.grid(row=20, column=0, sticky=W)
        print ('after pipe')

        submit = Button(self, text="Upload Data for Nodes", command=self.uploadEpanetDataNode)  # ('node'))
        submit.grid(row=21, column=0, sticky=W)
        submit = Button(self, text="Upload Data for Reservoir",
                        command=self.uploadEpanetDataReservoir)  # ('Reservoir'))
        submit.grid(row=22, column=0, sticky=W)

        print ('after upload data')




        # submit = Button(self, text="Upload CAD", command=self.uploadData)
        # submit.grid(row=21, column=0, sticky=W)

    def donothing(self):
        print ("work in progress")

    def uploadEpanetGraph(self):
        print ('b4 fileuploaf graph')

        path = self.fileupload()
        bard = Image.open(path)
        bard1 = bard.resize((550, 650), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard1)
        label1 = Label(self, image=bardejov, borderwidth=2, relief="solid")
        label1.image = bardejov
        label1.grid(row=3, column=2, columnspan=6, rowspan=40, sticky=E + W + S + N, padx=50, pady=15)

    def uploadEpanetDataPipe(self):
        print ('b4 fileuploaf data')

        path = self.fileupload()
        con = sqlite3.connect('pipe')
        cur = con.cursor()
        # path = '/Users/salonibindra/Desktop/output.csv'
        df = pandas.read_csv(path)
        df.to_sql('pipe', con, if_exists='append', index=False)
        node_name = cur.execute("Select DISTINCT Node_ID from pipe group by Node_ID")

        print ('b4 menubutton')
        mb = Menubutton(text="Node ID's", relief=RAISED)
        mb.grid(row=10, column=0, sticky=E)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mayoVar = IntVar()
        for x in node_name:
            mb.menu.add_checkbutton(label=x, variable=mayoVar)#, command=self.retrive_values(x))
        con.commit()
        con.close()
        print ('after commit ')


    def retrive_values(self, name_node):
        con = sqlite3.connect('node')
        cur = con.cursor()
        x = cur.execute("Select * from epanet where Node_ID = 'Node J-2'")

        data = list(cur.fetchall())
        con.commit()
        con.close()
        columns = ['Time', 'Elevation', 'Base Demand', 'Initial_Quality', 'Demand', 'Head', 'Pressure', 'Quality',
                   'Node_id']

        for r in range(25):
            for i in range(9):
                l = Label(text=data[r][i], relief=RIDGE)
                l.grid(row=r + 1, column=i + 2, sticky=NSEW)

        for d in range(len(columns)):
            l = Label(text=columns[d], relief=RIDGE)
            l.grid(row=0, column=d + 2, sticky=NSEW)


    def rawData(self, event):
        self.ind += 1

        # print (original_value)
        plt.clf()
        plt.subplot(211)
        ax = plt.gca()
        ax.plot(x, original_value, label='Raw-Values')
        plt.xlabel('TIme Series')
        plt.ylabel('Raw BioCon Values')
        plt.title('Raw Data in Time Series')
        plt.legend()

        # plt.ion()
        ax.figure.canvas.draw()

        analysisax = plt.axes([0.3, 0.3, 0.5, 0.075])
        analysisb = Button(analysisax, 'Continue with Analysis')
        ax.figure.canvas.draw()
        analysisb.on_clicked(self.analysis)

        timeseriesax = plt.axes([0.3, 0.2, 0.5, 0.075])
        time_seriesb = Button(timeseriesax, 'Time Series Range Update')
        ax.figure.canvas.draw()
        time_seriesb.on_clicked(self.select_time_series)

        back_ax = plt.axes([0.3, 0.1, 0.5, 0.075])
        back_but = Button(back_ax, 'Back')
        ax.figure.canvas.draw()
        back_but.on_clicked(self.stie_map)
        # self.show_buttons(event)
        plt.show()


def main():
    root = Tk()
    # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
    # root.winfo_screenheight()))
    root.geometry("900x700+200+250")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
        main()
