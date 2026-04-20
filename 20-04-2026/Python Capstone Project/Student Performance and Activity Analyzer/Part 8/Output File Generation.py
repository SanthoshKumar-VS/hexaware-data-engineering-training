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


final = {}

for s in students:
    name = s["name"]
    final[name] = {
        "marks": s["marks"],
        "course": s["course"],
        "attendance": attendance[name]
    }
with open("report.txt", "w") as sk:
    for n in final:
        sk.write(f"{n} - Marks: {final[n]['marks']} - Attendance: {final[n]['attendance']:.1f}%\n")
with open("report.txt", "w") as sk:
    sk.write("Student Report\n\n")

    for n in final:
        marks = final[n]["marks"]
        attendance_val = final[n]["attendance"]

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        sk.write(f"{n} - Marks: {marks} - Attendance: {attendance_val:.1f}% - Grade: {grade}\n")


eligible = [n for n in final if final[n]["marks"] >= 75 and final[n]["attendance"] >= 80]

with open("eligible_students.txt", "w") as sk:
    for n in eligible:
        sk.write(n + "\n")

