from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 1, 1),
}

dag = DAG(
    'crypto_data_pipeline',
    default_args=default_args,
    schedule_interval='@hourly',
)

producer_task = BashOperator(
    task_id='run_kafka_producer',
    bash_command='python /app/kafka/producer.py',
    dag=dag
)

spark_task = BashOperator(
    task_id='run_spark_stream',
    bash_command='spark-submit /app/spark/spark_streaming.py',
    dag=dag
)

producer_task >> spark_task
