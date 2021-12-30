'''
  Tarefa 3 Projeto: Desafio: Capturar dados de Loja de Aplicativo - Google Play
  Autor: Cícero Henrique dos Santos
  Descrição: Criar objeto com operações de captura de dados, com atualização da tabela. O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews. 
'''

class etl_with_gcp():

    #Função para capturar(extrair) dados no google play e enviar dados em arquivos csv para o Google Cloud Storage
    def scraper_google_play():
        # Ajustar código da tarefa 1 desenvolvido no colab para função  

    #Função para fazer download dos arquivos CSV do Google Cloud Storage
    def download_files_csv_cloud_storage():
        # Desenvolver lógica
        # Acessar bucket do cloud storage
        # Armazenar arquivos em uma lista
        # Fazer download dos arquivos da lista

    # Função para enviar Dataframes para o DataWarehouse(BigQuery) 
    def upload_dataframe_to_bigquery():
        # Desenvolver lógica
        # Ler cada arquivo csv e salvar em um Dataframe
        # Carregar DataFrames para tabela dentro do Datawarehouse(Bigquery)