import json
import csv
with open("../marks.json", "r") as sk:
    data = json.load(sk)
students = data["students"]

marks_list = [s["marks"] for s in students]

print("highest marks is:", max(marks_list))
print("lowest marks is:", min(marks_list))
print("sum of marks is:", sum(marks_list))

courses_tuple = tuple(s["course"] for s in students)
print("courses:", courses_tuple)

courses_set = set(courses_tuple)
print("unique courses:", courses_set)

marks_dict = {s["name"]: s["marks"] for s in students}
print("student marks dictionary:", marks_dict)

attendance = {}

with open("../attendance.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for row in reader:
        name = row["name"]
        percent = (int(row["days_present"]) / int(row["total_days"])) * 100
        attendance[name] = percent

print("student attendance dictionary:", attendance)