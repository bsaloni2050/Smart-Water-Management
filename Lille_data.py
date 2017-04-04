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

fig = plt.figure()
fig.suptitle("lille Data for January")


plt.subplot(221)
ax = plt.gca()
ax.plot(N_non_anomaly, 'o', color='g', label='Nonanomaly')
ax.plot(N_anomaly, 'o', color='r', label='Anomaly')
ax.axhline(y=1, color='k', label='1%')
ax.axhline(y=0.96, color='b', label=' 4%')
ax.axhline(y=0.9, color='c', label=' 10%')
ax.axhline(y=0.8, color='y', label=' 20%')
ax.axhline(y=0.7, color='r', label=' 30%')
plt.xlabel('Time Series')
plt.ylabel(' Delta F')
plt.title('Delta F v/s Time Series')
plt.legend(loc=1)

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
        if combine[i] > 0.96:
            likelihood[i] = 0.05
            likelihoodM[0][0].append(i)  # blue

        elif combine[i] <= 0.96 or combine[i] > 0.9:
            likelihood[i] = 0.2
            likelihoodM[1][0].append(i)  # green

        elif combine[i] <= 0.9 or combine[i] > 0.8:
            likelihood[i] = 0.2
            likelihoodM[2][0].append(i)  # green

        elif combine[i] <= 0.8 or combine[i] > 0.7:
            likelihood[i] = 0.45
            likelihoodM[3][0].append(i)  # yellow

        elif combine[i] <= 0.7:
            likelihood[i] = 0.45
            likelihoodM[4][0].append(i)  # yellow

    elif n == 'second hour':
        if combine[i] > 0.96:
            likelihood[i] = 0.05
            likelihoodM[0][1].append(i)  # blue

        elif combine[i] <= 0.96 or combine[i] > 0.9:
            likelihood[i] = 0.2
            likelihoodM[1][1].append(i)  # green

        elif combine[i] <= 0.9 or combine[i] > 0.8:
            likelihood[i] = 0.45
            likelihoodM[2][1].append(i)  # yellow

        elif combine[i] <= 0.8 or combine[i] > 0.7:
            likelihood[i] = 0.45
            likelihoodM[3][1].append(i)  # yellow

        elif combine[i] <= 0.7:
            likelihood[i] = 0.75
            likelihoodM[4][1].append(i)  # orange

    elif n == 'third hour':
        if combine[i] > 0.96:
            likelihood[i] = 0.05
            likelihoodM[0][2].append(i)  # blue

        elif combine[i] <= 0.96 or combine[i] > 0.9:
            likelihood[i] = 0.45
            likelihoodM[1][2].append(i)  # yellow

        elif combine[i] <= 0.9 or combine[i] > 0.8:
            likelihood[i] = 0.45
            likelihoodM[2][2].append(i)  # yellow

        elif combine[i] <= 0.8 or combine[i] > 0.7:
            likelihood[i] = 0.75
            likelihoodM[3][2].append(i)  # orange

        elif combine[i] <= 0.7:
            likelihood[i] = 0.75
            likelihoodM[4][2].append(i)  # orange

    elif n == 'fourth hour':
        if combine[i] > 0.96:
            likelihood[i] = 0.05
            likelihoodM[0][3].append(i)  # blue

        elif combine[i] <= 0.96 or combine[i] > 0.9:
            likelihood[i] = 0.45
            likelihoodM[1][3].append(i)  # yellow

        elif combine[i] <= 0.9 or combine[i] > 0.8:
            likelihood[i] = 0.75
            likelihoodM[2][3].append(i)  # orange

        elif combine[i] <= 0.8 or combine[i] > 0.7:
            likelihood[i] = 0.75
            likelihoodM[3][3].append(i)  # orange

        elif combine[i] <= 0.7:
            likelihood[i] = 0.9
            likelihoodM[4][3].append(i)  # red

    elif n == 'fifth hour':
        if combine[i] > 0.96:
            likelihood[i] = 0.05
            likelihoodM[0][4].append(i)  # blue

        elif combine[i] <= 0.96 or combine[i] > 0.9:
            likelihood[i] = 0.45
            likelihoodM[1][4].append(i)  # yellow

        elif combine[i] <= 0.9 or combine[i] > 0.8:
            likelihood[i] = 0.75
            likelihoodM[2][4].append(i)  # orange

        elif combine[i] <= 0.8 or combine[i] > 0.7:
            likelihood[i] = 0.9
            likelihoodM[3][4].append(i)  # red

        elif combine[i] <= 0.7:
            likelihood[i] = 0.9
            likelihoodM[4][4].append(i)  # red

# print (likelihoodM)
# Plot the Liklihood Matrix
plt.subplot(222)
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

plt.subplot(223)
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


# plotting the Normalized Data

# plt.subplot(212)
# plt.plot(N_non_anomaly, 'o', color='g')
# plt.plot(N_anomaly, 'o', color='r')
# plt.axhline(y=1, color='k')
# plt.axhline(y=0.96, color='b')
# plt.axhline(y=0.9, color='c')
# plt.axhline(y=0.8, color='y')
# plt.axhline(y=0.7, color='r')


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
plt.subplot(224)
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

plt.show()