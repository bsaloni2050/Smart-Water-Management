import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

im = np.arange(100)
im.shape = 10, 10

fig = plt.figure(1, (4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)

grid[1].imshow(im) # The AxesGrid object work as a list of axes.

plt.show()