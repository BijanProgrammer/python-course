import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(x, y, ls="--", color="g", linewidth=3)
plt.show()
