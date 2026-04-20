import json

with open("../products.json", "r") as sk:
    data = json.load(sk)

products = data["products"]

for s in products:
    print(s["name"], s["price"])

product_dict = {}
for s in products:
    product_dict[s["product_id"]] = {
        "name": s["name"],
        "price": s["price"]
    }
print("{")
for s in product_dict:
    print(f'  {s}: {{"name": "{product_dict[s]["name"]}", "price": {product_dict[s]["price"]}}},')
print("}")

expensive = max(products, key=lambda s: s["price"])
print("most expensive product:", expensive["name"])

cheap = min(products, key=lambda s: s["price"])
print("least expensive product:", cheap["name"])