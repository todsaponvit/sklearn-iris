import pandas as pd

df = pd.read_csv("iris.csv")
print(df.head())

print(df.species.value_counts())

print(df.columns)
