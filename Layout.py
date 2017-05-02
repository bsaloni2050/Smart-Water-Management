'''This is the Layout using Tkinder'''

from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style
from Tkinter import *
import tkMessageBox
import Tkinter
import os
from PIL import ImageTk, Image
import matplotlib as plt
matplotlib.use("TkAgg")
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Smart Water Management")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        #self.columnconfigure(3, pad=7)
        #self.rowconfigure(3, weight=1)
        #self.rowconfigure(5, pad=7)

        label2 = Label(self, text="Corporation Name: W-Smart")
        label2.grid(row=3, column=0, sticky=W)
        label3 = Label(self, text="Operator Name: Saloni")
        label3.grid(row=4, column=0, sticky=W)
        label4 = Label(self, text="Designation: Consultant")
        label4.grid(row=5, column=0, sticky=W)
        # label6 = Label(self, text="Application Name: ")
        # label6.grid(row=6, column=0, sticky=W)

        mb1 = Menubutton(self, text="Application Name  ", relief=RAISED)
        mb1.grid(row=12, column=0, sticky=W)
        mb1.menu = Menu(mb1, tearoff=0)
        mb1["menu"] = mb1.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb1.menu.add_checkbutton(label="BioCon", variable=mayoVar, command=self.epanet)
        mb1.menu.add_checkbutton(label="Net Leak", variable=ketchVar)
        mb1.menu.add_checkbutton(label="EnCon", variable=ketchVar)


        mb = Menubutton(self, text="Site Name", relief=RAISED)
        mb.grid(row=7, column=0, sticky=W)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb.menu.add_checkbutton(label="GIS", variable=mayoVar, command= self.launch_GIS)
        mb.menu.add_checkbutton(label="Google Earth", variable=ketchVar, command=self.launch_GoogleEarth)

        # submit = Button(self, text="Launch EPANET", command= self.launch)
        # submit.grid(row=17, column =0, sticky=W)

        bard = Image.open("sitemap.png")
        bard1 = bard.resize((550,650),Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard1)
        label1 = Label(self, image=bardejov, borderwidth=2, relief="solid")
        label1.image = bardejov
        label1.grid(row=3, column=2, columnspan=6, rowspan=40, sticky=E+W+S+N,padx=50, pady=15)

    def launch_GIS(self):
        #os.system("open /Applications/Safari.app")
        webbrowser.open("https://www.arcgis.com/home/index.html")


    def launch_GoogleEarth(self):
        webbrowser.open("https://earth.google.com/web/")

    def launch_Epanet(self):
        webbrowser.open("http://epanet.de/")


    def epanet(self):
        self.initUI()

        self.parent.title("Smart Water Management : BioCon")

        label2 = Label(self, text=" Application Name:  BioCon")
        label2.grid(row=12, column=0, sticky=W)

        submit = Button(self, text="Launch EPANET", command= self.launch_Epanet)
        submit.grid(row=14, column =0, sticky=W)

        mb = Menubutton(self, text="Data Analysis", relief=RAISED)
        mb.grid(row=16, column=0, sticky=W)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mayoVar = IntVar()
        ketchVar = IntVar()
        mb.menu.add_checkbutton(label="Spot Analysis", variable=mayoVar, command=self.launch_Epanet)
        mb.menu.add_checkbutton(label=" DMA", variable=ketchVar)

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