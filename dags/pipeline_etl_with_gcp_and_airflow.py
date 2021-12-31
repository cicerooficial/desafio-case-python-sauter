#   Example Pipeline definition
#   https://airflow.apache.org/docs/apache-airflow/1.10.1/tutorial.html#example-pipeline-definition

# Importa bibliotecas necessárias para criação desde Pipeline
import airflow
from airflow                                                import DAG
from datetime                                               import datetime, timedelta
from airflow.operators.python_operator                      import PythonOperator
from etl_with_gcp_and_airflow.etl_with_gcp_and_airflow      import etl_with_gcp

# Configurações de execução
default_args = {
    'owner':                'cicero',                               # Quem criou o pipeline
    'email':                ['cicerooficial@gmail.com'],            # Email do proprietário do Pipeline
    'email_on_failure':     ['cicerooficial@gmail.com'],            # Em caso de falha, envia notificação para o e-mail 
    'start_date':           datetime(2021, 12, 30),                 # Data de inicio do Pipeline
    'retry_delay':          timedelta(minutes=5),                   # Se falhar tenta novamente em 5 minutos
    'retries':              1                                       # Em casa de falha realiza mais uma tentativa
}

# Definição da DAG
dag = DAG(
    dag_id              =   'pipeline_etl_with_gcp_and_airflow',    # Nome do Pipeline                    
    default_args        =   default_args,                           # Argumentos padrão (definido acima)
    schedule_interval   =   timedelta(mounth=1),                    # Intervalo de cada execução
    catchup             =   False                                   # True executa a quantidade perdida de execução entre a data definida no start_date até o dia atual
)

# Chama as funções criadas através da importação classe etl_with_gcp
def scraper_google_play():                                          # Chama função scraper_google_play() através da classe etl_with_gcp
    etl_with_gcp().scraper_google_play()                            

def download_files_csv_cloud_storage():                             # Chama função download_files_csv_cloud_storage() através da classe etl_with_gcp
    etl_with_gcp().download_files_csv_cloud_storage()               

def upload_dataframe_to_bigquery():                                 # Chama função upload_dataframe_to_bigquery() através da classe etl_with_gcp
    etl_with_gcp().upload_dataframe_to_bigquery()

# Define as tarefas(tasks)
scraper_google_play = PythonOperator(
    task_id         =   'scraper_google_play',                      # Define o nome da tarefa(task)
    python_callable =   scraper_google_play,                        # Define o nome do objeto a ser chamado
    dag             =   dag                                         # Define a dag com as configurações de DAG criadas acima
)

download_files_csv_cloud_storage = PythonOperator(
    task_id         =   'download_files_csv_cloud_storage',         # Define o nome da tarefa(task)
    python_callable =   download_files_csv_cloud_storage,           # Define o nome do objeto a ser chamado
    dag             =   dag                                         # Define a dag com as configurações de DAG criadas acima
)

upload_dataframe_to_bigquery = PythonOperator(
    task_id         =   'upload_dataframe_to_bigquery',             # Define o nome da tarefa(task)
    python_callable =   upload_dataframe_to_bigquery,               # Define o nome do objeto a ser chamado
    dag             =   dag                                         # Define a dag com as configurações de DAG criadas acima
)

# Define a ordem das tasks (Pipeline) de acordo com o Design de arquitetura definido

scraper_google_play >> download_files_csv_cloud_storage >> upload_dataframe_to_bigquery