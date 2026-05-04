import dlt
from pyspark.sql.functions import *

@dlt.table
def new_gold_patient_summary():

    df = dlt.read("new_silver_patient_visit")

    result = df.groupBy("city","department") \
        .agg(
            count("visit_id").alias("total_patients"),
            sum("total_bill").alias("total_revenue")
        )

    return result