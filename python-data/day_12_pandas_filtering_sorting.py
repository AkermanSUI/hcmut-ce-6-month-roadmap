
import pandas as pd
df = pd.read_csv("python-data/students.csv")

df["average"] = (df["math"] + df["english"]) / 2

print(df)
print()

good_students = df[(df["average"] >= 8.0)]
print(good_students)
print(0)

good_math_students = df[(df["math"] >= 8.0) & (df["english"] >= 7.0)]
print(good_math_students)
print()


sorted_df = df.sort_values("average", ascending= False)
print(sorted_df)
print()


class_average = df["average"].mean()
print("class average:" ,class_average)
print()

highest_student = df["average"].max()
print("highest student:" ,highest_student)
print()

lowest_student = df["average"].min()
print("lowest student:" ,lowest_student)
print()

total_students = len(df)

df["status"] = "Fail"
df.loc[df["average"] >= 6.5, "status"] = "Pass"
print(df)
