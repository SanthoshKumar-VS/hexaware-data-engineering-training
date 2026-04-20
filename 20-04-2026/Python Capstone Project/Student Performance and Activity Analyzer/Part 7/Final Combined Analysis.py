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
        "attendance": attendance[name],
        "course": s["course"]
    }

print("{")

for name in final:
    print(f'  "{name}": {{"marks": {final[name]["marks"]}, "attendance": {final[name]["attendance"]:.1f}, "course": "{final[name]["course"]}"}},')

print("}")

for name in final:
    marks = final[name]["marks"]
    attendance_val = final[name]["attendance"]
    course = final[name]["course"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("name:", name)
    print("marks:", marks)
    print("attendance:", f"{attendance_val:.1f}%")
    print("course:", course)
    print("grade:", grade)
    print()


eligible = [n for n in final if final[n]["marks"] >= 75 and final[n]["attendance"] >= 80]
print("students who are eligible for certification is:", eligible)


improve = [n for n in final if final[n]["marks"] < 75 or final[n]["attendance"] < 80]
print("students who need improvement", improve)