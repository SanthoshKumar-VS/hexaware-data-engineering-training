import pandas as pd
import numpy as np


sales = pd.read_csv("data/sales.csv")

products = pd.read_csv("data/products.csv")

stores = pd.read_csv("data/stores.csv")


print(sales.head())



data = pd.merge(sales, products, on="product_id")

data = pd.merge(data, stores, on="store_id")



data["revenue"] = data["quantity"] * data["price"]

data["profit"] = data["revenue"] - (data["quantity"] * data["cost"])



print(data)



total = data.groupby("store_name")[["revenue","profit"]].sum()

print(total)



high_sales = data[data["revenue"] > 5000]

print(high_sales)



data.to_csv("output/final_sales.csv", index=False)

print("file saved")