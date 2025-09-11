import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/iris.csv")
print(df.head())

print(df.species.value_counts())

print(df.columns)

print(df.groupby("species").mean())

print(df.columns)

print(df.info())

# Train Dataset
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

test_size = 0.2
X_train, X_test, y_train, y_test = train_test_split(
    df[["sepal_length", "sepal_width", "petal_length", "petal_width"]],
    df.species,
    test_size=test_size,
    random_state=7,
)

print(X_train)


