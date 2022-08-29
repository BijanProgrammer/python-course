import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print()

print(df['grade'].mean())
print(df['grade'].median())
print(df['grade'].mode()[0])
