from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args={
    'owner':'sagar',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

def get_amazon_version():
    import airflow.providers.amazon
    print("amazon package ", {airflow.providers.amazon.__version__}," is available for aiflow") 

with DAG(
    dag_id='DAG-WITH-S3-CHECK_OBJECT_PRESENCE',
    start_date=datetime(2024,1,10),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    
    get_amazon=PythonOperator(
        task_id='get_amazon_version',
        python_callable=get_amazon_version
    )

    object_check=S3KeySensor(
        task_id='object_check',
        bucket_name='airflow-data',
        bucket_key='data.csv',
        aws_conn_id='minio_conn'
    )

    get_amazon >> object_check
