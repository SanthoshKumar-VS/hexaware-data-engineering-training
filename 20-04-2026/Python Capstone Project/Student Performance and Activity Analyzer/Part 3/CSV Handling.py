import csv

attendance = {}

with open("../attendance.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for row in reader:
        print(row["name"], row["days_present"], row["total_days"])

with open("../attendance.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for row in reader:
        name = row["name"]
        percent = (int(row["days_present"]) / int(row["total_days"])) * 100
        attendance[name] = percent
        print("attendance percentage:",name, percent)

low = [n for n in attendance if attendance[n] < 80]
print("students with attendance below 80% is",low)

best = max(attendance, key=attendance.get)
print("student with the best attendance is:",best)