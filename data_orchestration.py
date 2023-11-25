from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python import PythonOperator

print("INITIATING DATA ORCHESTRATION!")
# Function for data extraction
def extract_data():
    print('[1/3] EXTRACTING DATA..')
    with open('Data-Orchestration/source_data.csv', 'w') as file:
        file.write("Player_ID,Player_Name,Goals_Scored,Assists\n")
        file.write("1,John Doe,5,2\n")
        file.write("2,Jane Smith,3,4\n")
        file.write("3,Michael Johnson,2,1\n")
        file.write("4,Emily Davis,4,3\n")
        file.write("5,Chris Wilson,1,2\n")
    print("Data extraction completed.")

# Function for data transformation
def transform_data():
    print("[2/3] TRANSFORMING DATA")
    with open('Data-Orchestration/source_data.csv', 'r') as file:
        data = file.readlines()
        transformed_data = ["P_" + row.strip() if idx != 0 else row.strip() for idx, row in enumerate(data)]
    
    with open('Data-Orchestration/transformed_data.csv', 'w') as file:
        file.write('\n'.join(transformed_data))
    print("Data transformation completed.")

# Function for data loading
def load_data():
    print('[3/3] LOADING DATA')
    with open('Data-Orchestration/transformed_data.csv', 'r') as file:
        data = file.read()
        print("Loaded data:")
        print(data)

    print("Data loading completed.")

# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_workflow', default_args=default_args, schedule='@daily')
# DAG represents a workflow i.e. a collection of tasks

# Tasks for each step in the workflow
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

#Tasks are represented as operators
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

# Define task dependencies
extract_task >> transform_task >> load_task
# Load() depends on transform() and transform() depends on extract()

# Execute the tasks manually
extract_data()  # Execute data extraction
transform_data()  # Execute data transformation
load_data()  # Execute data loading