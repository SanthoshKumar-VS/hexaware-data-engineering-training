import json
import csv

with open("../website_visits.txt", "r") as sk:
    visits = [line.strip() for line in sk]

with open("../products.json", "r") as sk:
    data = json.load(sk)
products = data["products"]

with open("../orders.csv", "r") as sk:
    orders = list(csv.DictReader(sk))


product_dict = {}
for s in products:
    product_dict[s["product_id"]] = {
        "name": s["name"],
        "price": s["price"]
    }


total_revenue = 0
revenue_product = {}

for s in orders:
    pid = int(s["product_id"])
    qty = int(s["quantity"])

    pname = product_dict[pid]["name"]
    price = product_dict[pid]["price"]

    revenue = qty * price
    total_revenue += revenue

    revenue_product[pname] = revenue_product.get(pname, 0) + revenue


customer_spending = {}

for s in orders:
    cust = s["customer"]
    pid = int(s["product_id"])
    qty = int(s["quantity"])

    customer_spending[cust] = customer_spending.get(cust, 0) + qty * product_dict[pid]["price"]
top_customer = max(customer_spending, key=customer_spending.get)
with open("sales_report.txt", "w", encoding="utf-8") as sk:
    sk.write("E-Commerce Sales Report\n")

    sk.write(f"Total Website Visits: {len(visits)}\n")
    sk.write(f"Unique Visitors: {len(set(visits))}\n")

    sk.write(f"Total Revenue: {total_revenue}\n")

    sk.write(f"Top Customer: {top_customer}\n")

    sk.write("Product Sales\n")

    for s in revenue_product:
        sk.write(f"{s} → {revenue_product[s]}\n")