students = [
    {"name": "An", "math": 8.5, "english": 7.0},
    {"name": "Binh", "math": 6.0, "english": 8.0},
    {"name": "Chi", "math": 9.0, "english": 8.5},
    {"name": "Dung", "math": 5.5, "english": 6.0}
]


def calculate_average(student):
    return (student["math"] + student["english"]) / 2

def find_best_student(students):
    best_average = 0;
    best_student = None;
    for student in students:
        average = calculate_average(student)
        if (average >= best_average):
            best_average = average
            best_student = student
    return best_student
    
best = find_best_student(students)
print(best["name"], calculate_average(best))

def filter_students_by_average(students, thresold):
    result = []

    for student in students:
        average = calculate_average(student)
        if (average >= thresold):
            result.append(student)

    return result

good_students = filter_students_by_average(students, 8.0)

for student in good_students:
    print(student["name"], calculate_average(student))