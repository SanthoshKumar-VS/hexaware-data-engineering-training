@dlt.table(name="gold_category_revenue")
def gold_category_revenue():

    return dlt.read("silver_orders")\
    .groupBy("order_status")\
    .agg(
    sum("total_revenue")
    .alias("category_revenue")
    )