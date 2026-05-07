from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_marks_file():
    with open("/tmp/student_marks.txt", "w") as file:
        file.write("Math,80\n")
        file.write("Science,75\n")
        file.write("English,90\n")
        file.write("Python,95\n")

    print("Student marks file created")

def read_marks_file():
    with open("/tmp/student_marks.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())

def calculate_total():
    total = 0

    with open("/tmp/student_marks.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        subject, marks = line.strip().split(",")
        total += int(marks)

    print("Total Marks =", total)

def percentage_calculation():
    percentage = 340 / 4
    print("Percentage =", percentage)

def generate_result():
    with open("/tmp/result.txt", "w") as file:
        file.write("Student Result Summary\n")
        file.write("Total Marks = 340\n")
        file.write("Result = PASS\n")

    print("Result file created")

with DAG(
    dag_id="multitask_exercise_dag",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    create_marks_file_task = PythonOperator(
        task_id="create_marks_file",
        python_callable=create_marks_file
    )

    read_marks_file_task = PythonOperator(
        task_id="read_marks_file",
        python_callable=read_marks_file
    )

    calculate_total_task = PythonOperator(
        task_id="calculate_total",
        python_callable=calculate_total
    )

    percentage_calculation_task = PythonOperator(
        task_id="percentage_calculation",
        python_callable=percentage_calculation
    )

    generate_result_task = PythonOperator(
        task_id="generate_result",
        python_callable=generate_result
    )

    create_marks_file_task >> read_marks_file_task >> calculate_total_task >> percentage_calculation_task >> generate_result_task
