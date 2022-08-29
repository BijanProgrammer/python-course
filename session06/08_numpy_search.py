import numpy as np

numbers = np.array([4, 8, 15, 16, 23, 42, 23])

print(np.where(numbers == 23)[0])
print(np.where(numbers % 2 == 0)[0])
