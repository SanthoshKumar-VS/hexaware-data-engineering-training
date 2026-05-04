from pyspark.sql.functions import col, upper
@dlt.table
def new_silver_patient_visit():

    df = dlt.read("new_bronze_patient_visit")

    df = df.withColumn("department", upper(col("department")))

    df = df.withColumn("test_cost", col("number_of_tests") * 2000)

    df = df.withColumn("total_bill", col("consultation_fee") + col("test_cost"))

    return df