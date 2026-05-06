@dlt.table(
name="gold_city_revenue",
comment="Revenue by city"
)
def gold_city_revenue():

    return dlt.read("silver_patient_visits")\
    .groupBy("city")\
    .agg(
    sum("total_bill")
    .alias("total_revenue")
    )