import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python-data/student_scores.csv")

print("Original data:")
print(df)

class_average = df.groupby("class")["score"].mean()

class_average.plot(kind="bar")

plt.title("Average Score by Class")
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.show()

subject_average = df.groupby("subject")["score"].mean()

subject_average.plot(kind="bar")

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()

student_subject_scores = df.pivot(
    index="name",
    columns="subject",
    values="score"
)

print("Scores by student and subject:")
print(student_subject_scores)

student_subject_scores.plot(kind="bar")

plt.title("Scores by Student and Subject")
plt.xlabel("Student")
plt.ylabel("Score")
plt.show()