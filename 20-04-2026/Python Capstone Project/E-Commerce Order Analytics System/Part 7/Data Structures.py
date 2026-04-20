import json
import csv

with open("../website_visits.txt", "r") as sk:
    visits = [line.strip() for line in sk]

with open("../products.json", "r") as sk:
    data = json.load(sk)
products = data["products"]

with open("../orders.csv", "r") as sk:
    orders = list(csv.DictReader(sk))

print("list:")
for s in orders:
    print(s)

product_dict = {}
for s in products:
    product_dict[s["product_id"]] = {
        "name": s["name"],
        "price": s["price"]
    }

print("dictionary:")
print("{")
for s in product_dict:
    print(f'  {s}: {{"name": "{product_dict[s]["name"]}", "price": {product_dict[s]["price"]}}},')
print("}")


unique_visitors = set(visits)

print("set:")
for s in unique_visitors:
    print(s)

revenue_product = {}

for s in orders:
    pid = int(s["product_id"])
    qty = int(s["quantity"])

    pname = product_dict[pid]["name"]
    price = product_dict[pid]["price"]

    revenue_product[pname] = revenue_product.get(pname, 0) + qty * price

product_revenue_tuple = [(s, revenue_product[s]) for s in revenue_product]

print("tuple:")
for s in product_revenue_tuple:
    print(s)