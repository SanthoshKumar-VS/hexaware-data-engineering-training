import pandas as pd

sales = pd.read_csv("/dbfs/FileStore/sales.csv")

products = pd.read_csv("/dbfs/FileStore/products.csv")

final = pd.merge(sales, products, on="product_id")

final["total"] = final["quantity"] * final["price"]

print(final.head())

final.to_csv("/dbfs/FileStore/final_output.csv")