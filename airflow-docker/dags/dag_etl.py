from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# importa funções dos arquivos
from extract import extrair_dados 
from transform import transformar_dados
from load import carregar_dados  

# Definição da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 25),
    'retries': 1,
}

with DAG(
    dag_id='extrair_transformar_dados_csv', 
    default_args=default_args,
    schedule_interval=None,  # Executa manualmente
    catchup=False,
) as dag:
    
    # Tarefa de extração
    tarefa_extração = PythonOperator(
        task_id='extrair_dados',
        python_callable=extrair_dados,
    )

    # Tarefa de transformação
    tarefa_transformação = PythonOperator(
        task_id='transformar_dados',
        python_callable=transformar_dados,  # Chama a função de transformação
    )

      # Tarefa de carregamento
    tarefa_carregamento = PythonOperator(
        task_id='carregar_dados',
        python_callable=carregar_dados,  # Chama a função de carregamento
    )

    # Definindo a ordem das tarefas
    tarefa_extração >> tarefa_transformação >> tarefa_carregamento
