import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import matplotlib.axes as ax
import matplotlib.patches as patches

x = []
original_value = []
anomaly = []
non_anomaly = []
N_anomaly = []
N_non_anomaly = []
combine = []

workbook = xlrd.open_workbook('/Users/salonibindra/Desktop/BioCon.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name('Sheet1')

# print(sheet.col_values(0))

for cell in sheet.col(1):
    x.append(cell.value)
for cell in sheet.col(2):
    original_value.append(cell.value)

# print (original_value)
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x, original_value)

threshold = 145

# separating Anomaly Data
for data in original_value:
    if data < threshold:
        anomaly.append(data)
        non_anomaly.append(0)
    else:
        non_anomaly.append(data)
        anomaly.append(0)

# Calculating MU from the Non-Anomaly Data
sum1 = 0
count = 0
for data in non_anomaly:
    if data != 0:
        sum1 += data
        count += 1

mu = sum1 / count

# Normalizing the Data:
for data in non_anomaly:
    if data != 0:
        N_non_anomaly.append(data / mu)
    else:
        N_non_anomaly.append(np.nan)

for data in anomaly:
    if data != 0:
        N_anomaly.append(data / mu)
    else:
        N_anomaly.append(np.nan)

# Re-checking Data
print (N_non_anomaly[:])

sta = np.nanstd(N_non_anomaly);
print (sta)

#Combining the data
for i in N_anomaly:
    if N_anomaly == np.nan:
        combine.append(N_non_anomaly)
    else:
        combine.append(N_anomaly)

# plotting the Normalized Data

# plt.subplot(212)
# plt.plot(N_non_anomaly, 'o', color='g')
# plt.plot(N_anomaly, 'o', color='r')
# plt.axhline(y=1, color='k')
# plt.axhline(y=0.96, color='b')
# plt.axhline(y=0.9, color='c')
# plt.axhline(y=0.8, color='y')
# plt.axhline(y=0.7, color='r')


class Index(object):
    ind = 0

    def rawData(self, event):
        self.ind += 1

        # print (original_value)
        plt.clf()
        plt.subplot(211)
        ax = plt.gca()
        ax.plot(x, original_value)
        plt.xlabel('TIme Series')
        plt.ylabel('Raw BioCon Values')
        plt.title('Raw Data in Time Series')
        # plt.legend()
        #plt.imshow(image, extent=[x.min(), x.max(), original_value.min(), original_value.max()])
        # patches.Rectangle((0, 50), 0, 190, facecolor="red")
        # plt.add_patch(patches)
        #ax.add_patch(patches.Rectangle((0, 150), 20, 20,))
        ax.figure.canvas.draw()

        analysisax = plt.axes([0.3, 0.2, 0.4, 0.075])
        analysisb = Button(analysisax, 'analysis')
        #analysisb.on_clicked(Index.analysis(self))

    def analysis(self):
        # self.ind += 1
        plt.clf()
        plt.subplot(211)
        ax = plt.gca()
        ax.plot(N_non_anomaly, 'o', color='g')
        ax.plot(N_anomaly, 'o', color='r')
        ax.axhline(y=1, color='k')
        ax.axhline(y=0.96, color='b')
        ax.axhline(y=0.9, color='c')
        ax.axhline(y=0.8, color='y')
        ax.axhline(y=0.7, color='r')
        ax.figure.canvas.draw()

    def pg_1(self, event):
        ax.figure.canvas.draw()

    def likly(self):
        print ('i am in likey')

        for i in range(len(combine)):
            if i <= 10:
                n = 'first hour'
            elif i <= 20:
                n = 'second hour'
            elif i <= 30:
                n = 'third hour'
            elif i <= 40:
                n = 'fourth hour'
            elif i <= 50:
                 n = 'fifth hour'






callback = Index()
bioconAx = plt.axes([0.3, 0.7, 0.5, 0.075])
netLeakAx = plt.axes([0.3, 0.450, 0.5, 0.075])
energyconAx = plt.axes([0.3, 0.2, 0.5, 0.075])

biocon = Button(bioconAx, 'BioCon')
biocon.on_clicked(callback.rawData)

netleak = Button(netLeakAx, 'NetLeak')
netleak.on_clicked(callback.analysis)

energycon = Button(energyconAx, 'EnCon')
energycon.on_clicked(callback.rawData)

plt.show()
