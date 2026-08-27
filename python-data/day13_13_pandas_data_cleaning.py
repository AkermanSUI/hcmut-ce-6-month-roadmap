import pandas as pd
df = pd.read_csv("python-data/students_dirty.csv")
print("Original data:")
print(df)
print()

print("Missing value table:")

print(df.isnull().sum())

df["name"] = df["name"].str.strip()

df["name"] = df["name"].str.title()

df["math"] = df["math"].fillna(df["math"].mean())
df["english"] = df["english"].fillna(df["english"].mean())

df = df.drop_duplicates()
df["average"] = (df["math"] + df["english"]) / 2

print("Perfect table:")
print(df)
