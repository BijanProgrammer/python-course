import pandas as pd

# pd.options.display.max_rows = 5

df = pd.read_csv("data.csv")
print(df)
print()

print(df.head(5))
print()

print(df.tail(5))
print()

print(df.info())
