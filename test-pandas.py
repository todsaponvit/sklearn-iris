import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/iris.csv")
print(df.head())

print(df.species.value_counts())

print(df.columns)
