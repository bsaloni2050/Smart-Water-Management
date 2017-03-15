import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import matplotlib.axes as ax
import matplotlib.patches as patches
from BioConMain import rawData as bio


class Enterhere(object):

    def __init__(self):
        print ("cons")

        pass

    def main_method_h(event):
        print ("3")

        bioconAx = plt.axes([0.3, 0.7, 0.5, 0.075])
        netLeakAx = plt.axes([0.3, 0.450, 0.5, 0.075])
        energyconAx = plt.axes([0.3, 0.2, 0.5, 0.075])

        biocon = Button(bioconAx, 'BioCon')
        biocon.on_clicked(bio.rawData())

        netleak = Button(netLeakAx, 'NetLeak')
        netleak.on_clicked(self.analysis)

        energycon = Button(energyconAx, 'EnCon')
        energycon.on_clicked(self.likly)

        plt.show()

print ("1")
callback = Enterhere()
print ("cons out")
callback.main_method_h()
print ("2")

plt.show()