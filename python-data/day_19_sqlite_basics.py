import sqlite3

connection = sqlite3.connect("outputs/students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    class TEXT,
    subject TEXT,
    score REAL
)
""")

scores = [
    ("An", "A", "Math", 8.5),
    ("An", "A", "English", 7.0),
    ("Binh", "A", "Math", 6.0),
    ("Binh", "A", "English", 8.0),
    ("Chi", "B", "Math", 9.0),
    ("Chi", "B", "English", 8.5),
    ("Dung", "B", "Math", 5.5),
    ("Dung", "B", "English", 6.0),
    ("Long", "B", "Math", 7.0),
    ("Long", "B", "English", 6.5)
]

cursor.executemany("""
INSERT INTO student_scores (name, class, subject, score)
VALUES (?, ?, ?, ?)
""", scores)
connection.commit()
cursor.execute("SELECT * FROM student_scores")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("""
SELECT name, class, subject, score
FROM student_scores
WHERE score >= 8.0
""")

high_scores = cursor.fetchall()

for row in high_scores:
    print(row)

cursor.execute("""
SELECT name, AVG(score)
FROM student_scores
GROUP BY name
""")

student_average = cursor.fetchall()

for row in student_average:
    print(row)

connection.close()