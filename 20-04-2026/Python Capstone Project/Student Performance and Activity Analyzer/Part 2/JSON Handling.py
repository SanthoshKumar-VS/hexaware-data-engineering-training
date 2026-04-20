import json
with open("../marks.json", "r") as sk:
    data = json.load(sk)
students = data["students"]

for s in students:
    print(s["name"], s["marks"])

top = max(students, key=lambda x: x["marks"])
print("student with highest marks is:", top["name"])

low = min(students, key=lambda x: x["marks"])
print("student with lowest marks is:", low["name"])

avg = sum(s["marks"] for s in students) / len(students)
print("average marks is:", avg)

for s in students:
    if s["course"] == "Python":
        print("student enrolled in python:", s["name"])

course_count = {}
for s in students:
    c = s["course"]
    course_count[c] = course_count.get(c, 0) + 1
print("student count per course:", course_count)