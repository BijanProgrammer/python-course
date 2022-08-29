import pandas as pd

numbers = [4, 8, 15, 16, 23, 42]
series = pd.Series(numbers)
print(series)
print()

coordinates = [23, 42, 108]
series = pd.Series(coordinates, index=["x", "y", "z"])
print(series)
print()

grades = {
    "bijan": 20,
    "reza": 19,
    "ali": 19.5
}
series = pd.Series(grades)
print(series)
print()
