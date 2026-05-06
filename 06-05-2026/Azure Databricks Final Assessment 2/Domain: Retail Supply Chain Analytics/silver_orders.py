@dlt.table(name="silver_orders")
def silver_orders():

    return dlt.read("bronze_orders")\
    .filter(
    (col("quantity") > 0) &
    (col("order_status").isNotNull())
    ).withColumn(
    "total_revenue",
    col("quantity") * 1000
    )