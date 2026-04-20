with open("../students.txt", "r") as sk:
    names = [line.strip() for line in sk]

for n in names:
    print(n)

print("total number of entries:", len(names))

unique_names = set(names)
print("unique student names:", unique_names)

count = {}
for n in names:
    count[n] = count.get(n, 0) + 1
print("student name count:", count)

with open("unique_students.txt", "w") as sk:
    for n in unique_names:
        sk.write(n + "\n")