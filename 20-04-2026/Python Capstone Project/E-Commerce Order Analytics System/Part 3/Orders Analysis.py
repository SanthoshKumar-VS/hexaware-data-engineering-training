import csv

orders = []

with open("../orders.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for s in reader:
        orders.append(s)
        print(s)

product_qty = {}
customer_orders = {}

for s in orders:
    pid = int(s["product_id"])
    cust = s["customer"]
    qty = int(s["quantity"])

    product_qty[pid] = product_qty.get(pid, 0) + qty
    customer_orders[cust] = customer_orders.get(cust, 0) + 1

print("total quantity sold per product:", product_qty)
print("{")

for s in customer_orders:
    print(f'  "{s}": {customer_orders[s]},')

print("}")