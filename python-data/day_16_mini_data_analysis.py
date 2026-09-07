import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python-data/student_scores.csv")

print("Original data:")
print(df)

print()
print("Data info:")
print(df.info())

print()
print("Missing value:")
print(df.isnull().sum())

student_average = df.groupby("name")["score"].mean()
print(student_average)

best_student = student_average.idxmax()
best_score = student_average.max()

lowest_student = student_average.idxmin()
lowest_score = student_average.min()

print("Best student:", best_student, best_score)
print("Lowest student:", lowest_student, lowest_score)

subject_average = df.groupby("subject")["score"].mean()
print(subject_average)
class_average = df.groupby("class")["score"].mean()
print(class_average)

student_average.plot(kind="bar")

plt.title("Average Score by Student")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.show()

subject_average.plot(kind="bar")

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()

class_average.plot(kind="bar")

plt.title("Average Score by Class")
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.show()

# Insights:
# 1. Student with highest average score is ...
# 2. Student with lowest average score is ...
# 3. Class ... has higher average score.
# 4. Subject ... has higher average score.