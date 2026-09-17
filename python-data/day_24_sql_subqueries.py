import sqlite3 as plt
connection = plt.connect("outputs/students_join.db")
cursor = connection.cursor()
cursor.execute("""
SELECT AVG(score)
FROM scores
""")
overall_average = cursor.fetchall()[0]
print("Overall average:", overall_average)

print("Scores above overall average:")

cursor.execute("""
SELECT student_id, subject, score
FROM scores
WHERE score > (
    SELECT AVG(score)
    FROM scores
)
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("Students with scores above overall average:")

cursor.execute("""
SELECT s.name, sc.subject, sc.score
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
WHERE sc.score > (
    SELECT AVG(score)
    FROM scores
)
ORDER BY sc.score DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

print("Students whose average is above overall average:")

cursor.execute("""
SELECT s.name, AVG(sc.score) AS student_average
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.id, s.name
HAVING AVG(sc.score) > (
    SELECT AVG(score)
    FROM scores
)
ORDER BY student_average DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

print("Highest average student:")

cursor.execute("""
SELECT s.name, AVG(sc.score) AS student_average
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.id, s.name
ORDER BY student_average DESC
LIMIT 1
""")

row = cursor.fetchone()

print(row)
print()
print("Highest score records:")

cursor.execute("""
SELECT s.name, sc.subject, sc.score
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
WHERE sc.score = (
    SELECT MAX(score)
    FROM scores
)
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

print("Students with at least one score >= 8.5:")

cursor.execute("""
SELECT name, class
FROM students
WHERE id IN (
    SELECT student_id
    FROM scores
    WHERE score >= 8.5
)
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

print("Students with average score below overall average:")

cursor.execute("""
SELECT
    s.name,
    s.class,
    AVG(sc.score) AS average_score
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.id, s.name, s.class
HAVING AVG(sc.score) < (
    SELECT AVG(score)
    FROM scores
)
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

connection.close()