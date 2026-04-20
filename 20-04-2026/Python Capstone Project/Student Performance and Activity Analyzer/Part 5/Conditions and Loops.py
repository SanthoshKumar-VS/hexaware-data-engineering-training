import json
import csv

with open("../marks.json", "r") as sk:
    data = json.load(sk)

students = data["students"]

attendance = {}

with open("../attendance.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for row in reader:
        name = row["name"]
        percent = (int(row["days_present"]) / int(row["total_days"])) * 100
        attendance[name] = percent

for s in students:
    if s["marks"] >= 50:
        print(s["name"], "Pass")
    else:
        print(s["name"], "Fail")

for s in students:
    m = s["marks"]
    if m >= 90:
        g = "A"
    elif m >= 75:
        g = "B"
    elif m >= 50:
        g = "C"
    else:
        g = "Fail"

    print("Grade:", s["name"], g)

for s in students:
    name = s["name"]
    if s["marks"] > 80 and attendance[name] > 85:
        print("student with marks above 80 & attendance above 85%:", name)
