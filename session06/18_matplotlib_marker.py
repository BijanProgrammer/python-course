import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(x, y, marker="o", ms=23, mfc="g", mec="g")
plt.show()
