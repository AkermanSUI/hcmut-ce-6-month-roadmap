import sqlite3

connection = sqlite3.connect("outputs/students_join.db")
cursor = connection.cursor()
cursor.execute("""
SELECT COUNT(*)
FROM students
WHERE name = 'Minh'
""")

count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO students (name, class)
    VALUES (?, ?)
    """, ("Minh", "C"))

    connection.commit()
print("INNER JOIN:")

cursor.execute("""
SELECT s.name, s.class, sc.subject, sc.score
FROM students AS s
INNER JOIN scores AS sc
ON s.id = sc.student_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("LEFT JOIN:")

cursor.execute("""
SELECT s.name, s.class, sc.subject, sc.score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("LEFT JOIN:")

cursor.execute("""
SELECT s.name, s.class, sc.subject, sc.score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("Students without scores:")

cursor.execute("""
SELECT s.name, s.class
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
WHERE sc.student_id IS NULL
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
print("Average score for all students:")

cursor.execute("""
SELECT s.name, AVG(sc.score) AS average_score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.id, s.name
ORDER BY average_score DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()
cursor.execute("""
SELECT
    s.name,
    COALESCE(AVG(sc.score), 0) AS average_score
FROM students AS s
LEFT JOIN scores AS sc
ON s.id = sc.student_id
GROUP BY s.id, s.name
ORDER BY average_score DESC
""")