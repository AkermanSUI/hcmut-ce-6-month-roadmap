import sqlite3

connection = sqlite3.connect("outputs/students.db")
cursor = connection.cursor()

# 1. SELECT name, subject, score từ toàn bộ bảng
print("1. All name, subject, score:")

cursor.execute("""
SELECT name, subject, score
FROM student_scores
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 2. Lọc các dòng có score >= 8.0
print("2. Sinh vien co score >= 8.0:")

cursor.execute("""
SELECT name, subject, score
FROM student_scores
WHERE score >= 8.0
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 3. Lọc các dòng subject = 'Math'
print("3. Cac dong subject = 'Math':")

cursor.execute("""
SELECT name, class, subject, score
FROM student_scores
WHERE subject = 'Math'
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 4. Lọc Math và score >= 8.0
print("4. Math va score >= 8.0:")

cursor.execute("""
SELECT name, class, subject, score
FROM student_scores
WHERE subject = 'Math' AND score >= 8.0
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 5. Sắp xếp toàn bộ điểm giảm dần
print("5. Sap xep toan bo diem giam dan:")

cursor.execute("""
SELECT name, subject, score
FROM student_scores
ORDER BY score DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 6. Lấy top 3 điểm cao nhất
print("6. Top 3 diem cao nhat:")

cursor.execute("""
SELECT name, subject, score
FROM student_scores
ORDER BY score DESC
LIMIT 3
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 7. Tính average score theo name
print("7. Average score theo name:")

cursor.execute("""
SELECT name, AVG(score) AS average_score
FROM student_scores
GROUP BY name
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 8. Tính average score theo class
print("8. Average score theo class:")

cursor.execute("""
SELECT class, AVG(score) AS average_score
FROM student_scores
GROUP BY class
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 9. Tính average score theo subject
print("9. Average score theo subject:")

cursor.execute("""
SELECT subject, AVG(score) AS average_score
FROM student_scores
GROUP BY subject
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


# 10. Tìm sinh viên có average score >= 7.5 bằng HAVING
print("10. Sinh vien co average score >= 7.5:")

cursor.execute("""
SELECT name, AVG(score) AS average_score
FROM student_scores
GROUP BY name
HAVING AVG(score) >= 7.5
ORDER BY average_score DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

connection.close()