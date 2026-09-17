import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok = True)
connection = sqlite3.connect("outputs/students.db")

df = pd.read_sql_query(
    """SELECT name, class, subject, score
        FROM student_scores""",
        connection
)
print("Original data from SQL:")
print(df)

student_average_df = pd.read_sql_query("""
SELECT name, AVG(score) AS average_score
FROM student_scores
GROUP BY name
ORDER BY average_score DESC
""", connection)

print()
print("Average score by student:")
print(student_average_df)

class_average_df = pd.read_sql_query("""
SELECT class, AVG(score) AS average_score
FROM student_scores
GROUP BY class
ORDER BY average_score DESC
""", connection)

print()
print("Average score by class:")
print(class_average_df)

subject_average_df = pd.read_sql_query("""
SELECT subject, AVG(score) AS average_score
FROM student_scores
GROUP BY subject
ORDER BY average_score DESC
""", connection)

print()
print("Average score by subject:")
print(subject_average_df)

high_scores_df = pd.read_sql_query("""
SELECT name, class, subject, score
FROM student_scores
WHERE score >= 8.0
ORDER BY score DESC
""", connection)

print()
print("High score records:")
print(high_scores_df)

student_average_df.to_csv("outputs/sql_student_average.csv", index=False)
class_average_df.to_csv("outputs/sql_class_average.csv", index=False)
subject_average_df.to_csv("outputs/sql_subject_average.csv", index=False)
high_scores_df.to_csv("outputs/sql_high_scores.csv", index=False)

student_average_df.plot(
    x="name",
    y="average_score",
    kind="bar",
    legend=False
)

plt.title("Average Score by Student from SQL")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("outputs/sql_student_average_chart.png")
plt.close()

class_average_df.plot(
    x="class",
    y="average_score",
    kind="bar",
    legend=False
)

plt.title("Average Score by Class from SQL")
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("outputs/sql_class_average_chart.png")
plt.close()

connection.close()

print("SQL + Pandas analysis completed.")