import pandas as pd

students = {
    "first_name": ["bijan", "reza", "ali"],
    "last_name": ["eisapour", "eisapour", "karimi"],
    "age": [21, 23, 30]
}

df = pd.DataFrame(students)
print(df)
print()

print(df.loc[0])
print()

print(df.loc[[0, 1]])
