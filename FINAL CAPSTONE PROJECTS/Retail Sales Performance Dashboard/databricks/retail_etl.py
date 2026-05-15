import pandas as pd

sales = pd.read_csv("/Volumes/retailprojectworkspace/default/retailfiles/sales.csv")

products = pd.read_csv("/Volumes/retailprojectworkspace/default/retailfiles/products.csv")

data = pd.merge(sales, products, on="product_id")

data["total"] = data["quantity"] * data["price"]

print(data)

top = data.groupby("product_name")["total"].sum()

print(top)