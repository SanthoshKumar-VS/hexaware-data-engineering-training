@dlt.table(
name="bronze_patient_visits",
comment="Raw patient visit data"
)
def bronze_patient_visits():

    data = [
    (1,"Chennai","Cardiology",2000,"Completed"),
    (2,"Bengaluru","Neurology",1500,"Completed"),
    (3,"Hyderabad","Orthopedic",None,"Pending"),
    (4,"Chennai","Cardiology",-500,"Completed"),
    (5,"Mumbai","Dermatology",3000,"Completed")
    ]

    columns = [
    "visit_id",
    "city",
    "specialization",
    "bill_amount",
    "visit_status"
    ]

    return spark.createDataFrame(data,columns)