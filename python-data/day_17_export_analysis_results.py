import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("python-data/student_scores.csv")

print("Original data:")
print(df)

student_average = df.groupby("name")["score"].mean()
class_average = df.groupby("class")["score"].mean()
subject_average = df.groupby("subject")["score"].mean()

student_average_df = student_average.reset_index()
class_average_df = class_average.reset_index()
subject_average_df = subject_average.reset_index()

student_average_df.to_csv("outputs/student_average.csv", index=False)
class_average_df.to_csv("outputs/class_average.csv", index=False)
subject_average_df.to_csv("outputs/subject_average.csv", index=False)

student_average.plot(kind="bar")
plt.title("Average Score by Student")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("outputs/student_average_chart.png")
plt.close()

class_average.plot(kind="bar")
plt.title("Average Score by Class")
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("outputs/class_average_chart.png")
plt.close()

subject_average.plot(kind="bar")
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("outputs/subject_average_chart.png")
plt.close()

print("Export completed.")