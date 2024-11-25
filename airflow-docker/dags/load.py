import pandas as pd
from sqlalchemy import create_engine

def carregar_dados():
    """
    Lê os dados transformados de um arquivo CSV e carrega em uma tabela no banco de dados MySQL.
    """
    caminho_entrada = '/opt/airflow/data/dados_transformados.csv'
    
    #config conexão com o banco de dados MySQL
    mysql_user = 'airflow' 
    mysql_password = 'airflow'  
    mysql_host = 'mysql' 
    mysql_port = '3306'
    mysql_database = 'students' 

    #URL de conexão do MySQL
    connection_string = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"
    
    # Cria o engine de conexão com o banco de dados
    engine = create_engine(connection_string)
    
    try:
        # Lê o arquivo CSV de dados transformados
        df = pd.read_csv(caminho_entrada)

        # Insere os dados no banco de dados na tabela 'dados_transformados'
        df.to_sql('dados_students', con=engine, if_exists='replace', index=False)

        print(f"Dados carregados na tabela 'dados_transformados' no banco de dados {mysql_database}.")
    except Exception as e:
        print(f"Erro ao carregar os dados no banco de dados: {e}")
