import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=labels, startangle=90)
plt.legend(title="Four Fruits:")
plt.show()
