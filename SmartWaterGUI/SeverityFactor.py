import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import matplotlib.axes as ax
import matplotlib.patches as patches
import math

x = []
original_value = []
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
#print (N_non_anomaly[:])

sta = np.nanstd(N_non_anomaly)
#print (sta)

# print (N_anomaly)
# print (N_non_anomaly)

# Combining the data
for i in range(len(N_non_anomaly)):
    if math.isnan(N_anomaly[i]):
        combine.append(N_non_anomaly[i])
    else:
        combine.append(N_anomaly[i])
print (combine[:])


slope.append(0)
# Calculate the slope
for i in range(2, len(combine)):
    x1 = combine[i]-combine[i-1]
    slope.append(x1)

slope.append(0)
print (slope[:])
print (len(slope))
print (len(x))
print (len(combine))
severity = np.zeros(len(slope))

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


print (severityM)
#
# Plot the Severity  Matrix
plt.clf()
plt.subplot(222)
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
plt.show()

#
# # # working with Liklehood matrix
# # matrix = np.matrix(severityM)
# # print (matrix)
# # plt.subplot(222)
# # plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,10.5,0.5,10.5))
# # plt.colorbar()
# # plt.show()
