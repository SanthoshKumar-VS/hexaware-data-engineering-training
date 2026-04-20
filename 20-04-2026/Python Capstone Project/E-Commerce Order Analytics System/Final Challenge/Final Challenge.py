import csv

with open("../website_visits.txt", "r") as sk:
    visits = [line.strip() for line in sk]

with open("../orders.csv", "r") as sk:
    orders = list(csv.DictReader(sk))


visit_set = set(visits)

ordered_customers = set()
for s in orders:
    ordered_customers.add(s["customer"])

never_ordered = visit_set - ordered_customers

if never_ordered:
    print("visited but never ordered anything.:", ", ".join(never_ordered))
else:
    print("visitors who visited but never ordered: no one..all visitors placed orders")

visit_count = {}
for s in visits:
    visit_count[s] = visit_count.get(s, 0) + 1

ordered_once = [s for s in ordered_customers if visit_count.get(s, 0) <= 1]
print("customers who ordered but visited the website not more than once:", ", ".join(ordered_once))