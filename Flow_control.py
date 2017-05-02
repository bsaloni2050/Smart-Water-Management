import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import matplotlib.axes as ax
import matplotlib.patches as patches
from time import sleep
import math
import matplotlib.image as mpimg
import os
from matplotlib import gridspec
from matplotlib.offsetbox import AnchoredText



x = []
original_value = []
Normalized = []
anomaly = []
non_anomaly = []
N_anomaly = []
N_non_anomaly = []
combine = []
severityM = [[[] for row in range(5)] for row in range(5)]
slope = []

workbook = xlrd.open_workbook('/Users/salonibindra/Desktop/BioCon.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name('Sheet1')

for cell in sheet.col(1):
    x.append(cell.value)
for cell in sheet.col(2):
    original_value.append(cell.value)

threshold = 145

# separating Anomaly Data
for data in original_value:
    if data < threshold:
        anomaly.append(data)
        non_anomaly.append(0)
    else:
        non_anomaly.append(data)
        anomaly.append(0)

# Calculating average from the Non-Anomaly Data
sum1 = 0
count = 0
for data in non_anomaly:
    if data != 0:
        sum1 += data
        count += 1

mu = sum1 / count

# Normalizing the Data (combined):
for data in original_value:
    Normalized.append(data / mu)

# print (Normalized)

# Normalizing the Data (separately):
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

# calculate the first STD : round 1
upper_bound = 1 + np.nanstd(N_non_anomaly)
print (upper_bound)
# print (Normalized[1])

# Filter for non-anomaly Round :1

for i in range(len(Normalized)):
    if N_non_anomaly[i] < upper_bound:
        N_anomaly[i] = N_non_anomaly[i]
        N_non_anomaly[i] = np.nan
    elif N_anomaly[i] > upper_bound:
        N_anomaly[i] = np.nan
        N_non_anomaly[i] = N_anomaly[i]

# calculate the first STD : round 2
upper_bound2 = 1 + np.nanstd(N_non_anomaly)
print (upper_bound2)

# Filter for non-anomaly Round :2

for i in range(len(Normalized)):
    if N_non_anomaly[i] < upper_bound:
        N_anomaly[i] = N_non_anomaly[i]
        N_non_anomaly[i] = np.nan
    elif N_anomaly[i] > upper_bound:
        N_anomaly[i] = np.nan
        N_non_anomaly[i] = N_anomaly[i]

# print (N_anomaly)
# print (N_non_anomaly)




# Combining the data
for i in range(len(N_non_anomaly)):
    if math.isnan(N_anomaly[i]):
        combine.append(N_non_anomaly[i])
    else:
        combine.append(N_anomaly[i])

# sta = np.nanstd(combine, 2)
# sta2 = np.nanstd(sta)

# print (sta)
#print (combine)
# print (sta2)


# define likelihood, Severity ,Risk matrix
likelihood = np.zeros(len(combine))
severity = np.zeros(len(combine))
slope = np.zeros(len(combine))
risk = np.zeros(len(combine))
# likelihood = []
# slope = []
# risk = []
likelihoodM = [[[] for row in range(5)] for row in range(5)]
severityM = [[[] for row in range(5)] for row in range(5)]
riskM = [[[] for row in range(5)] for row in range(5)]

slope[0] = 0
# Calculate the slope
for i in range(2, len(combine)):
    x1 = combine[i] - combine[i - 1]
    slope[i] = (x1)

slope[len(combine) - 1] = 0


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

    def stie_map(self, event):
        self.ind += 1

        plt.clf()
        ax = plt.gca()

        plt.subplot(221)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(3, 8, 'boxed italics text in data coords', style='italic',
                bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

        
        plt.subplot(222)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        img = mpimg.imread('sitemap.png')
        plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off')
        plt.tick_params(axis='y', which='both', bottom='off', top='off', labelbottom='off', labeltop='off')
        plt.setp(ax.get_yticklabels(), visible=False)

        plt.imshow(img)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)


        analysisax1 = plt.axes([0.25, 0.1, 0.5, 0.075])
        analysisb1 = Button(analysisax1, 'View Data')
        analysisb1.on_clicked(self.rawData)

        epanetax = plt.axes([0.25, 0.3, 0.5, 0.075])
        epanetb = Button(epanetax, 'Launch EPANET')
        ax.figure.canvas.draw()
        epanetb.on_clicked(self.launch_Epanet)
        # self.show_buttons(event)
        plt.show()
        

    def launch_Epanet(self, event):
        self.ind += 1
        os.system("open /Applications/Safari.app")
        plt.show()

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

    def select_time_series(self, event):
        print ('')



    def analysis(self, event):
        self.ind += 1

        # Plot Normalized Data
        plt.clf()
        plt.subplot(211)
        ax = plt.gca()
        ax.plot(N_non_anomaly, 'o', color='g', label='Nonanomaly')
        ax.plot(N_anomaly, 'o', color='r',label='Anomaly')
        ax.axhline(y=1, color='k', label='1%')
        ax.axhline(y=0.96, color='b', label=' 4%')
        ax.axhline(y=0.9, color='c', label=' 10%')
        ax.axhline(y=0.8, color='y', label=' 20%')
        ax.axhline(y=0.7, color='r', label=' 30%')
        plt.xlabel('Time Series')
        plt.ylabel(' Delta F')
        plt.title('Delta F v/s Time Series')
        plt.legend(loc =1)
        ax.figure.canvas.draw()

        likx = plt.axes([0.3, 0.4, 0.5, 0.075])
        likb = Button(likx, 'Likelihood Indicator')
        ax.figure.canvas.draw()

        likb.on_clicked(self.likelihood_call)

        sevx = plt.axes([0.3, 0.3, 0.5, 0.075])
        sevb = Button(sevx, 'Severity Indicator')
        ax.figure.canvas.draw()
        sevb.on_clicked(self.severity_call)

        riskx = plt.axes([0.3, 0.2, 0.5, 0.075])
        riskb = Button(riskx, 'Risk Indicator')
        ax.figure.canvas.draw()
        riskb.on_clicked(self.risk_call)

        back_ax = plt.axes([0.3, 0.1, 0.5, 0.075])
        back_but = Button(back_ax, 'Back')
        ax.figure.canvas.draw()
        back_but.on_clicked(self.stie_map)

        ax.figure.canvas.draw()
        plt.show()

    def change_indicators(self, event, insignificant, low, moderate, high):
        print ("nothing")







    def likelihood_call(self, event):

        self.ind += 1
        plt.clf()

        insignificant = 0.96
        low = 0.9
        moderate = 0.8
        high = 0.7

        # Calculate the likelihood Matrix
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

            if n == 'first hour':
                if combine[i] > insignificant:
                    likelihood[i] = 0.05
                    likelihoodM[0][0].append(i)  # blue

                elif combine[i] <= insignificant or combine[i] > low:
                    likelihood[i] = 0.2
                    likelihoodM[1][0].append(i)  # green

                elif combine[i] <= low or combine[i] > moderate:
                    likelihood[i] = 0.2
                    likelihoodM[2][0].append(i)  # green

                elif combine[i] <= moderate or combine[i] > high:
                    likelihood[i] = 0.45
                    likelihoodM[3][0].append(i)  # yellow

                elif combine[i] <= high:
                    likelihood[i] = 0.45
                    likelihoodM[4][0].append(i)  # yellow

            elif n == 'second hour':
                if combine[i] > insignificant:
                    likelihood[i] = 0.05
                    likelihoodM[0][1].append(i)  # blue

                elif combine[i] <= insignificant or combine[i] > low:
                    likelihood[i] = 0.2
                    likelihoodM[1][1].append(i)  # green

                elif combine[i] <= low or combine[i] > moderate:
                    likelihood[i] = 0.45
                    likelihoodM[2][1].append(i)  # yellow

                elif combine[i] <= moderate or combine[i] > high:
                    likelihood[i] = 0.45
                    likelihoodM[3][1].append(i)  # yellow

                elif combine[i] <= high:
                    likelihood[i] = 0.75
                    likelihoodM[4][1].append(i)  # orange

            elif n == 'third hour':
                if combine[i] > insignificant:
                    likelihood[i] = 0.05
                    likelihoodM[0][2].append(i)  # blue

                elif combine[i] <= insignificant or combine[i] > low:
                    likelihood[i] = 0.45
                    likelihoodM[1][2].append(i)  # yellow

                elif combine[i] <= low or combine[i] > moderate:
                    likelihood[i] = 0.45
                    likelihoodM[2][2].append(i)  # yellow

                elif combine[i] <= moderate or combine[i] > high :
                    likelihood[i] = 0.75
                    likelihoodM[3][2].append(i)  # orange

                elif combine[i] <= high:
                    likelihood[i] = 0.75
                    likelihoodM[4][2].append(i)  # orange

            elif n == 'fourth hour':
                if combine[i] > insignificant:
                    likelihood[i] = 0.05
                    likelihoodM[0][3].append(i)  # blue

                elif combine[i] <= insignificant or combine[i] > low:
                    likelihood[i] = 0.45
                    likelihoodM[1][3].append(i)  # yellow

                elif combine[i] <= low or combine[i] > moderate:
                    likelihood[i] = 0.75
                    likelihoodM[2][3].append(i)  # orange

                elif combine[i] <= moderate or combine[i] > high:
                    likelihood[i] = 0.75
                    likelihoodM[3][3].append(i)  # orange

                elif combine[i] <= high:
                    likelihood[i] = 0.9
                    likelihoodM[4][3].append(i)  # red

            elif n == 'fifth hour':
                if combine[i] > insignificant:
                    likelihood[i] = 0.05
                    likelihoodM[0][4].append(i)  # blue

                elif combine[i] <= insignificant or combine[i] > low:
                    likelihood[i] = 0.45
                    likelihoodM[1][4].append(i)  # yellow

                elif combine[i] <= low or combine[i] > moderate:
                    likelihood[i] = 0.75
                    likelihoodM[2][4].append(i)  # orange

                elif combine[i] <= moderate or combine[i] > high:
                    likelihood[i] = 0.9
                    likelihoodM[3][4].append(i)  # red

                elif combine[i] <= high:
                    likelihood[i] = 0.9
                    likelihoodM[4][4].append(i)  # red

        # print (likelihoodM)
        # Plot the Liklihood Matrix
        plt.clf()
        plt.subplot(221)
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((0, 0.9), len(combine), 0.1, facecolor="red"))
        ax.add_patch(patches.Rectangle((0, 0.6), len(combine), 0.3, facecolor="orange"))
        ax.add_patch(patches.Rectangle((0, 0.3), len(combine), 0.3, facecolor="yellow"))
        ax.add_patch(patches.Rectangle((0, 0.1), len(combine), 0.2, facecolor="blue"))
        ax.add_patch(patches.Rectangle((0, 0), len(combine), 0.1, facecolor="green"))
        ax.plot(x, likelihood, color="black", linewidth=1.5)
        plt.xlabel('TIme Series')
        plt.ylabel('Liklihood Scale')
        plt.title('Liklihood Indicator')

        ax.figure.canvas.draw()

        likx = plt.axes([0.05, 0.10, 0.275, 0.075])
        likb = Button(likx, 'Likelihood Indicator')
        ax.figure.canvas.draw()

        likb.on_clicked(self.likelihood_call)

        sevx = plt.axes([0.375, 0.10, 0.275, 0.075])
        sevb = Button(sevx, 'Severity Indicator')
        ax.figure.canvas.draw()
        sevb.on_clicked(self.severity_call)

        riskx = plt.axes([0.7, 0.10, 0.275, 0.075])
        riskb = Button(riskx, 'Risk Indicator')
        ax.figure.canvas.draw()
        riskb.on_clicked(self.risk_call)

        plt.subplot(222)
        ax1 = plt.gca()

        plt.title('Liklihood Indicator Scale')
        img1 = mpimg.imread('Likelihood Indicator.png')
        plt.imshow(img1)
        ax1.figure.canvas.draw()
        labely = ['0-0',' Detla F','0-4%', '4-10%', '10-20%', '20-30%', '>30%']
        labelx = [1, 2, 3, 4, 5 ]
        ax1.set_xticklabels(labelx)
        ax1.set_yticklabels(labely)


        update_ind = plt.axes([0.6, 0.5, 0.275, 0.075])
        update_ind_b = Button(update_ind, 'Update Indicator Scale')
        ax.figure.canvas.draw()
        update_ind_b.on_clicked(self.update_indc)

        plt.show()

    def update_indc(self, event):
        plt.clf()
        ax = plt.gca()

        anchored_text = AnchoredText("Test", loc=2)
        ax.add_artist(anchored_text)

        plt.show()

    def severity_call(self, event):

        insignificant = 0.96
        low = 0.9
        moderate = 0.8
        high = 0.7

        for i in range(len(slope)):
            if i <= 6:
                n = 'first hour'
            elif i <= 18:
                n = 'second hour'
            elif i <= 60:
                n = 'third hour'
            elif i <= 140:
                n = 'fourth hour'
            elif i <= 250:
                n = 'fifth hour'

            if n == 'first hour':
                if slope[i] > insignificant:
                    severity[i] = 0.05
                    severityM[0][0].append(i)  # blue

                elif slope[i] <= insignificant or slope[i] > low:
                    severity[i] = 0.2
                    severityM[1][0].append(i)  # green

                elif slope[i] <= low or slope[i] > moderate:
                    severity[i] = 0.2
                    severityM[2][0].append(i)  # green

                elif slope[i] <= moderate or slope[i] > high:
                    severity[i] = 0.45
                    severityM[3][0].append(i)  # yellow

                elif slope[i] <= high:
                    severity[i] = 0.45
                    severityM[4][0].append(i)  # yellow

            elif n == 'second hour':
                if slope[i] > insignificant:
                    severity[i] = 0.05
                    severityM[0][1].append(i)  # blue

                elif slope[i] <= insignificant or slope[i] > low:
                    severity[i] = 0.2
                    severityM[1][1].append(i)  # green

                elif slope[i] <= low or slope[i] > moderate:
                    severity[i] = 0.45
                    severityM[2][1].append(i)  # yellow

                elif slope[i] <= moderate or slope[i] > high:
                    severity[i] = 0.45
                    severityM[3][1].append(i)  # yellow

                elif slope[i] <= high:
                    severity[i] = 0.75
                    severityM[4][1].append(i)  # orange

            elif n == 'third hour':
                if slope[i] > insignificant:
                    severity[i] = 0.05
                    severityM[0][2].append(i)  # blue

                elif slope[i] <= insignificant or slope[i] > low:
                    severity[i] = 0.45
                    severityM[1][2].append(i)  # yellow

                elif slope[i] <= low or slope[i] > moderate:
                    severity[i] = 0.45
                    severityM[2][2].append(i)  # yellow

                elif slope[i] <= moderate or slope[i] > high:
                    severity[i] = 0.75
                    severityM[3][2].append(i)  # orange

                elif slope[i] <= high:
                    severity[i] = 0.75
                    severityM[4][2].append(i)  # orange

            elif n == 'fourth hour':
                if slope[i] > insignificant:
                    severity[i] = 0.05
                    severityM[0][3].append(i)  # blue

                elif slope[i] <= insignificant or slope[i] > low:
                    severity[i] = 0.45
                    severityM[1][3].append(i)  # yellow

                elif slope[i] <= low or slope[i] > moderate:
                    severity[i] = 0.75
                    severityM[2][3].append(i)  # orange

                elif slope[i] <= moderate or slope[i] > high:
                    severity[i] = 0.75
                    severityM[3][3].append(i)  # orange

                elif slope[i] <= high:
                    severity[i] = 0.9
                    severityM[4][3].append(i)  # red

            elif n == 'fifth hour':
                if slope[i] > insignificant:
                    severity[i] = 0.05
                    severityM[0][4].append(i)  # blue

                elif slope[i] <= insignificant or slope[i] > low:
                    severity[i] = 0.45
                    severityM[1][4].append(i)  # yellow

                elif slope[i] <= low or slope[i] > moderate:
                    severity[i] = 0.75
                    severityM[2][4].append(i)  # orange

                elif slope[i] <= moderate or slope[i] > high:
                    severity[i] = 0.9
                    severityM[3][4].append(i)  # red

                elif slope[i] <= high:
                    severity[i] = 0.9
                    severityM[4][4].append(i)  # red

        # Plot the Severity  Matrix
        plt.clf()
        plt.subplot(221)
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((0, low), len(slope), 0.1, facecolor="red"))
        ax.add_patch(patches.Rectangle((0, 0.6), len(slope), 0.3, facecolor="orange"))
        ax.add_patch(patches.Rectangle((0, 0.3), len(slope), 0.3, facecolor="yellow"))
        ax.add_patch(patches.Rectangle((0, 0.1), len(slope), 0.2, facecolor="blue"))
        ax.add_patch(patches.Rectangle((0, 0), len(slope), 0.1, facecolor="green"))
        ax.plot(x, severity, color="black", linewidth=1.5)
        plt.xlabel('TIme Series')
        plt.ylabel('Severity Scale')
        plt.title('Severity Indicator')
        ax.figure.canvas.draw()

        likx = plt.axes([0.05, 0.10, 0.275, 0.075])
        likb = Button(likx, 'Likelihood Indicator')
        ax.figure.canvas.draw()

        likb.on_clicked(self.likelihood_call)

        sevx = plt.axes([0.375, 0.10, 0.275, 0.075])
        sevb = Button(sevx, 'Severity Indicator')
        ax.figure.canvas.draw()
        sevb.on_clicked(self.severity_call)

        riskx = plt.axes([0.7, 0.10, 0.275, 0.075])
        riskb = Button(riskx, 'Risk Indicator')
        ax.figure.canvas.draw()
        riskb.on_clicked(self.risk_call)


        plt.subplot(222)
        ax1 = plt.gca()

        plt.title('Severity Indicator Scale')
        #plt.tick_params(axis='y', which='both', bottom='off', top='off', labelbottom='off')
        img1 = mpimg.imread('Likelihood Indicator.png')
        plt.imshow(img1)
        ax1.figure.canvas.draw()
        labely = ['0-0',' Detla F','0-4%', '4-10%', '10-20%', '20-30%', '>30%']

        labelx = ['0-1','1-2','2-3','3-4','4-5']

        ind = [1,3,6,9,13]  # the x locations for the groups
        #plt.xticks(ind,labelx)

        ax1.set_xticklabels(labelx)
        ax1.set_yticklabels(labely)


        update_ind = plt.axes([0.6, 0.5, 0.275, 0.075])
        update_ind_b = Button(update_ind, 'Update Indicator Scale')
        ax.figure.canvas.draw()
        update_ind_b.on_clicked(self.update_indc)

        ax.figure.canvas.draw()
        plt.show()

    def risk_call(self, event):

        insignificant = 0.05
        low = 0.2
        moderate = 0.45
        high = 0.75
        very_high = 0.9

        for i in range(len(combine)):
            if likelihood[i] == 0.05:
                n = 'blue'
            elif likelihood[i] == 0.2:
                n = 'green'
            elif likelihood[i] == 0.45:
                n = 'yellow'
            elif likelihood[i] == 0.75:
                n = 'orange'
            elif likelihood[i] == 0.9:
                n = 'red'

            if n == 'blue':
                if severity[i] == insignificant:
                    risk[i] = 0.05
                    riskM[0][0].append(i)  # blue

                elif severity[i] == low:
                    risk[i] = 0.05
                    riskM[1][0].append(i)  # blue

                elif severity[i] == moderate:
                    risk[i] = 0.05
                    riskM[2][0].append(i)  # blue

                elif severity[i] == high:
                    risk[i] = 0.05
                    riskM[3][0].append(i)  # blue

                elif severity[i] == very_high:
                    risk[i] = 0.05
                    riskM[4][0].append(i)  # blue

            elif n == 'green':
                if severity[i] == insignificant:
                    risk[i] = 0.2
                    riskM[0][1].append(i)  # green

                elif severity[i] == low:
                    risk[i] = 0.2
                    riskM[1][1].append(i)  # green

                elif severity[i] == moderate:
                    risk[i] = 0.45
                    riskM[2][1].append(i)  # yellow

                elif severity[i] == high:
                    risk[i] = 0.45
                    riskM[3][1].append(i)  # yellow

                elif severity[i] == very_high:
                    risk[i] = 0.75
                    riskM[4][1].append(i)  # orange

            elif n == 'yellow':
                if severity[i] == insignificant:
                    risk[i] = 0.2
                    riskM[0][2].append(i)  # green

                elif severity[i] == low:
                    risk[i] = 0.45
                    riskM[1][2].append(i)  # yellow

                elif severity[i] == moderate:
                    risk[i] = 0.45
                    riskM[2][2].append(i)  # yellow

                elif severity[i] == high:
                    risk[i] = 0.75
                    riskM[3][2].append(i)  # orange

                elif severity[i] == very_high:
                    risk[i] = 0.75
                    riskM[4][2].append(i)  # orange

            elif n == 'orange':
                if severity[i] == insignificant:
                    risk[i] = 0.45
                    riskM[0][3].append(i)  # yellow

                elif severity[i] == low:
                    risk[i] = 0.45
                    riskM[1][3].append(i)  # yellow

                elif severity[i] == moderate:
                    risk[i] = 0.75
                    riskM[2][3].append(i)  # orange

                elif severity[i] == high:
                    risk[i] = 0.75
                    riskM[3][3].append(i)  # orange

                elif severity[i] == very_high:
                    risk[i] = 0.9
                    riskM[4][3].append(i)  # red

            elif n == 'red':
                if severity[i] == insignificant:
                    risk[i] = 0.45
                    riskM[0][4].append(i)  # yellow

                elif severity[i] == low:
                    risk[i] = 0.75
                    riskM[1][4].append(i)  # orange

                elif severity[i] == moderate:
                    risk[i] = 0.75
                    riskM[2][4].append(i)  # orange

                elif severity[i] == high:
                    risk[i] = 0.9
                    riskM[3][4].append(i)  # red

                elif severity[i] == very_high:
                    risk[i] = 0.9
                    riskM[4][4].append(i)  # red

        # Plot the Risk  Matrix
        plt.clf()
        plt.subplot(221)
        ax = plt.gca()
        ax.add_patch(patches.Rectangle((0, 0.9), len(slope), 0.1, facecolor="red"))
        ax.add_patch(patches.Rectangle((0, 0.6), len(slope), 0.3, facecolor="orange"))
        ax.add_patch(patches.Rectangle((0, 0.3), len(slope), 0.3, facecolor="yellow"))
        ax.add_patch(patches.Rectangle((0, 0.1), len(slope), 0.2, facecolor="blue"))
        ax.add_patch(patches.Rectangle((0, 0), len(slope), 0.1, facecolor="green"))
        ax.plot(x, risk, color="black", linewidth=1.5)
        plt.xlabel('TIme Series')
        plt.ylabel('Risk Scale')
        plt.title('Risk Indicator')
        ax.figure.canvas.draw()


        likx = plt.axes([0.05, 0.10, 0.275, 0.075])
        likb = Button(likx, 'Likelihood Indicator')
        ax.figure.canvas.draw()

        likb.on_clicked(self.likelihood_call)

        sevx = plt.axes([0.375, 0.10, 0.275, 0.075])
        sevb = Button(sevx, 'Severity Indicator')
        ax.figure.canvas.draw()
        sevb.on_clicked(self.severity_call)

        riskx = plt.axes([0.7, 0.10, 0.275, 0.075])
        riskb = Button(riskx, 'Risk Indicator')
        ax.figure.canvas.draw()
        riskb.on_clicked(self.risk_call)


        plt.subplot(222)
        ax1 = plt.gca()

        plt.title('Risk Indicator Scale')
        #plt.tick_params(axis='y', which='both', bottom='off', top='off', labelbottom='off')
        img1 = mpimg.imread('Likelihood Indicator.png')
        plt.imshow(img1)
        ax1.figure.canvas.draw()
        labely = ['0-0',' Detla F','0-10%', '10-30%', '30-60%', '60-90%', '>90%']

        labelx = [1,2,3,4,5]

        ind = [1,3,6,9,13]  # the x locations for the groups
        #plt.xticks(ind,labelx)

        ax1.set_xticklabels(labelx)
        ax1.set_yticklabels(labely)


        update_ind = plt.axes([0.6, 0.5, 0.275, 0.075])
        update_ind_b = Button(update_ind, 'Update Indicator Scale')
        ax.figure.canvas.draw()
        update_ind_b.on_clicked(self.update_indc)
        ax.figure.canvas.draw()
        plt.show()

    def show_buttons(self, event):

        plt.axes('off')
        plt.clf()
        ax = plt.gca()
        ax.figure.canvas.draw()
        analysisax = plt.axes([0.05, 0.015, 0.25, 0.075])
        analysisb = Button(analysisax, 'Likelihood Indicator')
        analysisb.on_clicked(self.likelihood_call)
        ax.figure.canvas.draw()

        analysisax = plt.axes([0.35, 0.015, 0.25, 0.075])
        analysisb = Button(analysisax, 'Severity Indicator')
        analysisb.on_clicked(self.severity_call)
        ax.figure.canvas.draw()

        analysisax = plt.axes([0.65, 0.015, 0.25, 0.075])
        analysisb = Button(analysisax, 'Risk Indicator')
        ax.figure.canvas.draw()
        analysisb.on_clicked(self.risk_call)


callback = Index()
bioconAx = plt.axes([0.3, 0.7, 0.5, 0.075])
netLeakAx = plt.axes([0.3, 0.450, 0.5, 0.075])
energyconAx = plt.axes([0.3, 0.2, 0.5, 0.075])

biocon = Button(bioconAx, 'BioCon')
biocon.on_clicked(callback.stie_map)

netleak = Button(netLeakAx, 'NetLeak')
netleak.on_clicked(callback.stie_map)

energycon = Button(energyconAx, 'EnOpt')
energycon.on_clicked(callback.show_buttons)

plt.show()
