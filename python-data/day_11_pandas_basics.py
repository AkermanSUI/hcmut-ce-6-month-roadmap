import pandas as pd

df = pd.read_csv("python-data/students.csv")

print("Students table:")
print(df)

print(df["name"])

df["average"] = (df["math"] + df["english"]) / 2

best_index = df["average"].idxmax()
best_student = df.loc[best_index]

print(best_student["name"], best_student["average"])
good_student = df[df["average"] >= 8.0]
for index, student in good_student.iterrows():
    print(student["name"], student["average"])