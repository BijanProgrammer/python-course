import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

for cell in np.nditer(matrix):
    print(cell)
