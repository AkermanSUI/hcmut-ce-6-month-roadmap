students = [
    {"name": "An", "math": 8.5, "english": 7.0},
    {"name": "Binh", "math": 6.0, "english": 8.0},
    {"name": "Chi", "math": 9.0, "english": 8.5},
    {"name": "Dung", "math": 5.5, "english": 6.0}
]

# 1. In tên từng sinh viên
for student in students:
    print(student["name"])

# 2. Tính điểm trung bình của từng sinh viên
for student in students:
    average = (student["math"] + student["english"]) / 2
    print(student["name"], average)

# 3. In sinh viên có điểm trung bình cao nhất
best_student = None
best_average = 0
for student in students:
    average = (student["math"] + student["english"]) / 2
    if average > best_average:
        best_average = average
        best_student = student
print("Sinh viên có điểm trung bình cao nhất:", best_student["name"])

# 4. In danh sách sinh viên có điểm trung bình >= 8.0

students_above_8 = []
for student in students:
    average = (student["math"] + student["english"]) / 2
    if average >= 8.0:
        students_above_8.append(student["name"])

print("Danh sach sinh vien co diem trung binh >= 8.0:", students_above_8)