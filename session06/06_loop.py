import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

for row in matrix:
    print(row)
    
    for cell in row:
        print(cell)
    
    print()
