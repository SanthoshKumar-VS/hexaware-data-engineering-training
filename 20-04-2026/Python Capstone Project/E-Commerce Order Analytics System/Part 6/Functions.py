import json
import csv

def load_visits():
    with open("../website_visits.txt", "r") as sk:
        return [line.strip() for line in sk]

visits = load_visits()
for s in visits:
    print(s)


def load_products():
    with open("../products.json", "r") as sk:
        return json.load(sk)["products"]

products = load_products()

print("{")
for s in products:
    print(f'  {s["product_id"]}: {{"name": "{s["name"]}", "price": {s["price"]}}},')
print("}")


def load_orders():
    with open("../orders.csv", "r") as sk:
        return list(csv.DictReader(sk))

orders = load_orders()

for s in orders:
    print(s)


product_dict = {}
for s in products:
    product_dict[s["product_id"]] = {
        "name": s["name"],
        "price": s["price"]
    }


def calculate_product_revenue(orders, product_dict):
    revenue = {}
    for s in orders:
        pid = int(s["product_id"])
        qty = int(s["quantity"])

        pname = product_dict[pid]["name"]
        price = product_dict[pid]["price"]

        revenue[pname] = revenue.get(pname, 0) + qty * price
    return revenue


product_revenue = calculate_product_revenue(orders, product_dict)

print("product revenue""{")
for s in product_revenue:
    print(f'  "{s}": {product_revenue[s]},')
print("}")


def calculate_customer_spending(orders, product_dict):
    spending = {}
    for s in orders:
        cust = s["customer"]
        pid = int(s["product_id"])
        qty = int(s["quantity"])

        spending[cust] = spending.get(cust, 0) + qty * product_dict[pid]["price"]
    return spending


customer_spending = calculate_customer_spending(orders, product_dict)

print("customer spendings" "{")
for s in customer_spending:
    print(f'  "{s}": {customer_spending[s]},')
print("}")


def top_customer(spending):
    return max(spending, key=spending.get)


top = top_customer(customer_spending)

print("top customer is:",top)
