import sqlite3

connection = sqlite3.connect("outputs/day_26_constraints.db")

connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS scores")
cursor.execute("DROP TABLE IF EXISTS students")


cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK(age >= 18)
)
""")

cursor.execute("""
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    score REAL CHECK(score >= 0 AND score <= 10),

    UNIQUE(student_id, subject)
    FOREIGN KEY (student_id)
    REFERENCES students(id)
)
""")

students = [
    ("An", "an@gmail.com", 19),
    ("Binh", "binh@gmail.com", 20),
    ("Chi", "chi@gmail.com", 18)
]

cursor.executemany("""
INSERT INTO students (name, email, age)
VALUES (?, ?, ?)
""", students)

connection.commit()

cursor.execute("""
SELECT *
FROM students
""")

for row in cursor.fetchall():
    print(row)



scores = [
    (1, "Math", 8.5),
    (1, "English", 7.0),
    (2, "Math", 6.5),
    (3, "Math", 9.0)
]

cursor.executemany("""
INSERT INTO scores (student_id, subject, score)
VALUES (?, ?, ?)
""", scores)

connection.commit()

cursor.execute("""
SELECT
    s.name,
    sc.subject,
    sc.score
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
""")

for row in cursor.fetchall():
    print(row)

try:
    cursor.execute("""
    INSERT INTO scores (student_id, subject, score)
    VALUES (?, ?, ?)
    """, (1, "Math", 9.5))

    connection.commit()

except sqlite3.IntegrityError as error:
    print("Duplicate subject error:", error)