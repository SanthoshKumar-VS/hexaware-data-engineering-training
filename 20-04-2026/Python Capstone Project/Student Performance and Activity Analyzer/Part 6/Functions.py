import json
import csv
with open("../marks.json", "r") as sk:
    data = json.load(sk)
students = data["students"]

attendance = {}
with open("../attendance.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for row in reader:
        attendance[row["name"]] = (int(row["days_present"]) / int(row["total_days"])) * 100


def read_names():
    with open("../students.txt", "r") as sk:
        return [line.strip() for line in sk]

print("Student names:", read_names())


def avg_marks(students):
    return sum(s["marks"] for s in students) / len(students)

print("Average marks:", avg_marks(students))

def calculate_attendance_percentage(days_present, total_days):
    return (days_present / total_days) * 100
print("Attendance percentage:", calculate_attendance_percentage(22, 25))

def topper(students):
    return max(students, key=lambda x: x["marks"])

print("Topper:", topper(students)["name"])


def grade_func(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 50:
        return "C"
    else:
        return "Fail"

print("Sample grade:", grade_func(85))