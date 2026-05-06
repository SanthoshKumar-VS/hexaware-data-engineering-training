import dlt
from pyspark.sql.functions import *

@dlt.table(name="bronze_orders")
def bronze_orders():

    data = [
    (301,101,201,"2024-04-01",20,"Delivered"),
    (302,102,201,"2024-04-01",35,"Delivered"),
    (303,111,204,"2024-04-02",2,"Delivered"),
    (304,114,208,"2024-04-02",5,"Pending"),
    (305,115,204,"2024-04-03",3,"Delivered"),
    (306,104,202,"2024-04-03",50,"Delivered"),
    (307,105,202,"2024-04-04",18,"Cancelled")
    ]

    columns = [
    "order_id",
    "product_id",
    "supplier_id",
    "order_date",
    "quantity",
    "order_status"
    ]

    return spark.createDataFrame(
    data,columns
    )