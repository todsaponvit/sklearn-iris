import pandas as pd

df = pd.read_csv("iris.csv")
print(df.head())

print(df.variety.value_counts())

print(df.columns)
