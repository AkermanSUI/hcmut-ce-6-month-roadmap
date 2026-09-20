import sqlite3

connection = sqlite3.connect("outputs/students_join.db")
cursor = connection.cursor()


# 1. INSERT student
cursor.execute("""
INSERT INTO students (name, class)
VALUES (?, ?)
""", ("Hoa", "C"))

connection.commit()


# 2. SELECT
print("After INSERT:")

cursor.execute("""
SELECT *
FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 3. UPDATE student
cursor.execute("""
UPDATE students
SET class = ?
WHERE name = ?
""", ("D", "Hoa"))

print("Rows updated:", cursor.rowcount)

connection.commit()


# 4. SELECT after UPDATE
print("After UPDATE:")

cursor.execute("""
SELECT *
FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 5. DELETE student
cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Hoa",))

connection.commit()


# 6. SELECT after DELETE
print("After DELETE:")

cursor.execute("""
SELECT *
FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 7. INSERT score
cursor.execute("""
INSERT INTO scores (student_id, subject, score)
VALUES (?, ?, ?)
""", (5, "Physics", 8.0))

connection.commit()


# 8. UPDATE score
cursor.execute("""
UPDATE scores
SET score = ?
WHERE student_id = ? AND subject = ?
""", (8.5, 5, "Physics"))

connection.commit()


# 9. DELETE score
cursor.execute("""
DELETE FROM scores
WHERE student_id = ? AND subject = ?
""", (5, "Physics"))

connection.commit()


# 10. Challenge - tìm ID của Dung
cursor.execute("""
SELECT id
FROM students
WHERE name = ?
""", ("Dung",))

dung_id = cursor.fetchone()[0]


# Tăng tất cả điểm của Dung thêm 0.5
cursor.execute("""
UPDATE scores
SET score = score + 0.5
WHERE student_id = ?
""", (dung_id,))

print("Dung scores updated:", cursor.rowcount)

connection.commit()


# Kiểm tra điểm của Dung
cursor.execute("""
SELECT s.name, sc.subject, sc.score
FROM students AS s
JOIN scores AS sc
ON s.id = sc.student_id
WHERE s.name = ?
""", ("Dung",))

for row in cursor.fetchall():
    print(row)


connection.close()