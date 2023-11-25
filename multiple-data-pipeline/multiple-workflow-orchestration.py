from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Default arguments for the DAGs
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG 1: First Data Processing Workflow
dag_1 = DAG('data_pipeline_1', default_args=default_args, schedule_interval='@daily')

def extract_data_1():
    with open('/path/to/data_source_1.csv', 'r') as file:
        data = file.read()
        print(f"Extracted data from CSV 1: {data}")

def transform_data_1():
    # Simulated transformation
    print("Transformed data for CSV 1.")

def load_data_1():
    # Simulated loading
    print("Loaded data from CSV 1.")

extract_task_1 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data_1,
    dag=dag_1
)

transform_task_1 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_1,
    dag=dag_1
)

load_task_1 = PythonOperator(
    task_id='load_data',
    python_callable=load_data_1,
    dag=dag_1
)

extract_task_1 >> transform_task_1 >> load_task_1

# DAG 2: Second Data Processing Workflow
dag_2 = DAG('data_pipeline_2', default_args=default_args, schedule_interval='@weekly')

def extract_data_2():
    with open('/path/to/data_source_2.csv', 'r') as file:
        data = file.read()
        print(f"Extracted data from CSV 2: {data}")

def transform_data_2():
    # Simulated transformation
    print("Transformed data for CSV 2.")

def load_data_2():
    # Simulated loading
    print("Loaded data from CSV 2.")

extract_task_2 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data_2,
    dag=dag_2
)

transform_task_2 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_2,
    dag=dag_2
)

load_task_2 = PythonOperator(
    task_id='load_data',
    python_callable=load_data_2,
    dag=dag_2
)

extract_task_2 >> transform_task_2 >> load_task_2
