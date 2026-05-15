import pandas as pd

sales = pd.read_csv("data/sales.csv")
products = pd.read_csv("data/products.csv")
stores = pd.read_csv("data/stores.csv")

print(sales.head())

data = pd.merge(sales, products, on="product_id")
data = pd.merge(data, stores, on="store_id")

data["revenue"] = data["quantity"] * data["price"]
data["profit"] = data["revenue"] - data["cost"]

print(data)

summary = data.groupby("store_name")[["revenue", "profit"]].sum()

print(summary)

low_sales = data[data["revenue"] < 10000]

print(low_sales)

summary.to_csv("output/sales_summary.csv")

print("File saved")