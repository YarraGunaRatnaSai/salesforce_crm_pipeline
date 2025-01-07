from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_data():
    print("Extracting data from source...")

def transform_data():
    print("Transforming data...")

def load_to_salesforce():
    print("Loading data into Salesforce Data Cloud...")

with DAG(
    'etl_to_salesforce',
    default_args={'owner': 'airflow', 'start_date': datetime(2024, 12, 1)},
    schedule_interval='@daily'
) as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract_data)
    transform = PythonOperator(task_id='transform', python_callable=transform_data)
    load = PythonOperator(task_id='load', python_callable=load_to_salesforce)

    extract >> transform >> load
