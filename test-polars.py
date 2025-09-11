import polars as pl

df = pl.read_csv("iris.csv")
print(df.head())
