from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email_on_retry': False,
    'email': ['admin@example.com'],  # Add your email here
}

# Define the DAG
with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')

    generate_report = BashOperator(
        task_id='generate_report',
        bash_command='python /path/to/generate_report.py'
    )

    send_alert = BashOperator(
        task_id='send_alert',
        bash_command='python /path/to/send_alert.py'
    )

    failure_email = EmailOperator(
        task_id='send_failure_email',
        to='admin@example.com',  # Add your email here
        subject='Task Failed',
        html_content='Task {{ task_instance.task_id }} in DAG {{ dag.dag_id }} failed.',
        trigger_rule='one_failed',  # Trigger email on failure of any task
    )

    end = DummyOperator(task_id='end')

    # Set the task dependencies
    start >> generate_report >> send_alert >> end
    send_alert >> failure_email
