import os
import pandas as pd

os.makedirs("outputs", exist_ok=True)


df = pd.read_csv("python-data/student_scores.csv")

print("Original data:")
print(df)

total_records = len(df)
total_students = df["name"].nunique()

student_average = df.groupby("name")["score"].mean()
class_average = df.groupby("class")["score"].mean()
subject_average = df.groupby("subject")["score"].mean()

best_student = student_average.idxmax()
best_score = student_average.max()

lowest_student = student_average.idxmin()
lowest_score = student_average.min()

with open("outputs/student_report.md", "w", encoding="utf-8") as file:
    file.write("# Student Score Report\n")

    file.write("\n## Average Score by Student\n\n")

    for name, score in student_average.items():
        file.write(f"- {name}: {score}\n")
    file.write("\n## Average Score by Class\n\n")

    for class_name, score in class_average.items():
        file.write(f"- Class {class_name}: {score}\n")

    file.write("\n## Average Score by Subject\n\n")

    for subject, score in subject_average.items():
        file.write(f"- {subject}: {score}\n")

    file.write("\n## Insights\n\n")
    file.write(f"- {best_student} has the highest average score.\n")
    file.write(f"- {lowest_student} has the lowest average score.\n")
print("Report generated successfully.")