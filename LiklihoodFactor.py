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
likelihoodM = [[[] for row in range(5)] for row in range(5)]

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

print (x)
#print (combine[:])

likelihood = np.zeros(len(combine))

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
#print (likelihoodM)
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
plt.show()

#
# # working with Liklehood matrix
# matrix = np.matrix(likelihoodM)
# print (matrix)
# plt.subplot(222)
# plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,10.5,0.5,10.5))
# plt.colorbar()
# plt.show()
