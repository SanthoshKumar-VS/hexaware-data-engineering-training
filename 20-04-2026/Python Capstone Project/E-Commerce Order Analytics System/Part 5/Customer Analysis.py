import json
import csv

with open("../products.json", "r") as sk:
    data = json.load(sk)
products = data["products"]

product_dict = {}
for s in products:
    product_dict[s["product_id"]] = s["price"]

orders = []
with open("../orders.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for s in reader:
        orders.append(s)

customer_spending = {}

for s in orders:
    cust = s["customer"]
    pid = int(s["product_id"])
    qty = int(s["quantity"])

    customer_spending[cust] = customer_spending.get(cust, 0) + qty * product_dict[pid]

print("total spending per customer:", customer_spending)

top_customer = max(customer_spending, key=customer_spending.get)
print("highest spending customer.", top_customer)

high_spenders = [s for s in customer_spending if customer_spending[s] > 50000]
print("Customers spending more than 50000:", ", ".join(high_spenders))