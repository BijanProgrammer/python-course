import pandas as pd

df = pd.read_csv("data.csv")
# result = df.dropna()
df.dropna(inplace=True)
print(df)
