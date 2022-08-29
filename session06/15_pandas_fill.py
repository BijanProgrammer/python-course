import pandas as pd

df = pd.read_csv("data.csv")
average = df['Calories'].mean()
df.fillna(average, inplace=True)
print(df)
