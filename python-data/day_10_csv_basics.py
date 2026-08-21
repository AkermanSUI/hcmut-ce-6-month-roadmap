import csv


def calculate_average(student):
    # student là 1 dict đọc từ CSV
    # return average
    math = float(student["math"])
    english = float(student["english"])
    average = (math+english)/2
    return average

def read_students_from_csv(file_path):
    # đọc file CSV
    # return danh sách students
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    return students

def find_best_student(students):
    # return student có average cao nhất
    best_student = None
    best_average = 0

    for student in students:
        average = calculate_average(student)
        if ( average > best_average):
            best_average = average
            best_student = student
    return best_student
    

def filter_students_by_average(students, threshold):
    # return danh sách student có average >= threshold
    acc_student = []
    for student in students:
        average = calculate_average(student) 
        if (average >= threshold):
            acc_student.append(student)
    return acc_student        


students = read_students_from_csv("python-data/students.csv")

print("Student averages:")
for student in students:
    print(student["name"], calculate_average(student))

best = find_best_student(students)

print()
print("Best student: ")
print (best["name"], calculate_average(best))

print()
print ("Danh sach >= 8.0:")
goods_student = filter_students_by_average(students, 8.0)
for student in goods_student:
    print(student["name"], calculate_average(student))
