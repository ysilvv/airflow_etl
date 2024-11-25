import pandas as pd

def extrair_dados():
    """
    Lendo os dados de um arquivo e salva em um novo arquivo CSV com os dados extraídos.
    """
    caminho_entrada = '/opt/airflow/data/student-mat.parquet'

    
    # lê o arquivo Parquet
    df = pd.read_parquet(caminho_entrada)
    
    # salva os dados que foram extraídos em um arquivo CSV
    caminho_saida = '/opt/airflow/data/dados_extraidos.csv'
    df.to_csv(caminho_saida, index=False)
    
    print(f"Dados extraídos de {caminho_entrada} e salvos em {caminho_saida}.")
