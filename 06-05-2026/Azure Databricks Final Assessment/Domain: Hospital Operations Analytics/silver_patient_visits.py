@dlt.table(
name="silver_patient_visits",
comment="Cleaned patient visit data"
)
def silver_patient_visits():

    return dlt.read("bronze_patient_visits")\
    .filter(
    (col("bill_amount").isNotNull()) &
    (col("bill_amount") > 0)
    ).withColumn(
    "total_bill",
    col("bill_amount") + 500
    )