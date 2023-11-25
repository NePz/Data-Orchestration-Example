from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

print("ORCHESTRATING...")
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_workflow', default_args=default_args, schedule='@daily')

extract_task = BashOperator(
    task_id='extract_data',
    bash_command='extractData.py extract',
    dag=dag
)

transform_task = BashOperator(
    task_id='transform_data',
    bash_command='transformData.py transform',
    dag=dag
)

load_task = BashOperator(
    task_id='load_data',
    bash_command='loadData.py load',
    dag=dag
)

extract_task >> transform_task >> load_task
