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

final = {}
for s in students:
    name = s["name"]
    final[name] = {
        "marks": s["marks"],
        "attendance": attendance[name],
        "course": s["course"]
    }

topper = max(final, key=lambda x: final[x]["marks"])
print("Topper:", topper)

best_attendance = max(final, key=lambda x: final[x]["attendance"])
print("Best attendance:", best_attendance)

avg = sum(final[n]["marks"] for n in final) / len(final)
print("Average marks:", avg)

eligible = [n for n in final if final[n]["marks"] >= 75 and final[n]["attendance"] >= 80]
print("Eligible students:", eligible)

improve = [n for n in final if final[n]["marks"] < 75 or final[n]["attendance"] < 80]
print("Students needing improvement:", improve)