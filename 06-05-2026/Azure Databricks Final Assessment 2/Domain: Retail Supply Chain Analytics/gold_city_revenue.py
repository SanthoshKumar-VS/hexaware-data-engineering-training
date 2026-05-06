@dlt.table(name="gold_city_revenue")
def gold_city_revenue():

    return dlt.read("silver_orders")\
    .groupBy("supplier_id")\
    .agg(
    sum("total_revenue")
    .alias("city_revenue")
    )