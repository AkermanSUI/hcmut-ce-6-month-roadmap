import pandas as pd

# 1. Đọc file CSV
df = pd.read_csv("python-data/student_scores.csv")

print("Original data:")
print(df)

print()

# 2. Tính điểm trung bình theo class
class_average = df.groupby("class")["score"].mean()

print("Average score by class:")
print(class_average)

print()

# 3. Tính điểm trung bình theo subject
subject_average = df.groupby("subject")["score"].mean()

print("Average score by subject:")
print(subject_average)

print()

# 4. Tìm điểm cao nhất theo class
class_max = df.groupby("class")["score"].max()

print("Max score by class:")
print(class_max)

print()

# 5. Tìm điểm thấp nhất theo subject
subject_min = df.groupby("subject")["score"].min()

print("Min score by subject:")
print(subject_min)

print()

# 6. Đếm số dòng dữ liệu của từng class
class_count = df.groupby("class")["score"].count()

print("Number of scores by class:")
print(class_count)

print()

# 7. Tạo bảng tổng hợp mean, max, min theo class
class_summary = df.groupby("class")["score"].agg(["mean", "max", "min"])

print("Class summary:")
print(class_summary)