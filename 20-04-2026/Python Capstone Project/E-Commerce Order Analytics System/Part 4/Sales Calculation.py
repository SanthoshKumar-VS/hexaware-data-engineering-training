import json
import csv

with open("../products.json", "r") as sk:
    data = json.load(sk)
products = data["products"]

product_dict = {}
for s in products:
    product_dict[s["product_id"]] = {
        "name": s["name"],
        "price": s["price"]
    }

orders = []
with open("../orders.csv", "r") as sk:
    reader = csv.DictReader(sk)
    for s in reader:
        orders.append(s)

print("Revenue for each order:")

for s in orders:
    pid = int(s["product_id"])
    qty = int(s["quantity"])
    price = product_dict[pid]["price"]

    revenue = qty * price
    print(f'Order {s["order_id"]}: {revenue}')

total_revenue = 0

for s in orders:
    pid = int(s["product_id"])
    qty = int(s["quantity"])
    price = product_dict[pid]["price"]

    total_revenue += qty * price

print("Total revenue:", total_revenue)

revenue_product = {}

for s in orders:
    pid = int(s["product_id"])
    qty = int(s["quantity"])

    pname = product_dict[pid]["name"]
    price = product_dict[pid]["price"]

    revenue_product[pname] = revenue_product.get(pname, 0) + qty * price

print("{")

for s in revenue_product:
    print(f'  "{s}": {revenue_product[s]},')

print("}")

top_product = max(revenue_product, key=revenue_product.get)
print("highest selling product:", top_product)