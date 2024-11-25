import pandas as pd

def transformar_dados():
    """
    Lendo os dados extraídos, e fazendo a transformação das colunas e salvando em um novo arquivo CSV.
    """
    caminho_entrada = '/opt/airflow/data/dados_extraidos.csv'  
    
    # le o arquivo de entrada
    df = pd.read_csv(caminho_entrada)
    
    # dicionario que mapeia o nome das colunas em inglws para portugues
    traducao_colunas = {
        "school": "escola",
        "sex": "sexo",
        "age": "idade",
        "address": "endereco",
        "famsize": "tamanho_familia",
        "studytime": "tempo_estudo",
        "paid": "aulas_pagas",
        "freetime": "tempo_livre",
        "absences": "faltas",
        "G1": "nota_1_periodo",
        "G2": "nota_2_periodo",
        "G3": "nota_final"
    }
    
    # renomeia as colunas conforme o mapeamento
    df = df.rename(columns=traducao_colunas)
    
    # seleciona apenas essas colunas
    colunas_necessarias = [
        "escola", "sexo", "idade", "endereco", "tamanho_familia", "tempo_estudo",
        "aulas_pagas", "tempo_livre", "faltas", "nota_1_periodo", "nota_2_periodo", "nota_final"
    ]
    df = df[colunas_necessarias]
    
    # salva os dados transformados em um novo arquivo 
    caminho_saida = '/opt/airflow/data/dados_transformados.csv'
    df.to_csv(caminho_saida, index=False)
    
    print(f"Dados transformados e salvos em {caminho_saida}.")
