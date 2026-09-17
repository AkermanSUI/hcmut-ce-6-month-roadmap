import sqlite3

connection = sqlite3.connect("outputs/students_join.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS scores")
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    class TEXT
)
""")

cursor.execute("""
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    score REAL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

students = [
    ("An", "A"),
    ("Binh", "A"),
    ("Chi", "B"),
    ("Dung", "B"),
    ("Long", "B")
]

cursor.executemany("""
INSERT INTO students (name, class)
VALUES (?, ?)
""", students)

scores = [
    (1, "Math", 8.5),
    (1, "English", 7.0),
    (2, "Math", 6.0),
    (2, "English", 8.0),
    (3, "Math", 9.0),
    (3, "English", 8.5),
    (4, "Math", 5.5),
    (4, "English", 6.0),
    (5, "Math", 7.0),
    (5, "English", 6.5)
]

cursor.executemany("""
INSERT INTO scores (student_id, subject, score)
VALUES (?, ?, ?)
""", scores)

connection.commit()
print("Students table:")

cursor.execute("""
SELECT *
FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

print("Scores table:")

cursor.execute("""
SELECT *
FROM scores
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("Joined student scores:")

cursor.execute("""
SELECT students.name, students.class, scores.subject, scores.score
FROM students
JOIN scores
ON students.id = scores.student_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("High scores with student info:")

cursor.execute("""
SELECT students.name, students.class, scores.subject, scores.score
FROM students
JOIN scores
ON students.id = scores.student_id
WHERE scores.score >= 8.0
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
