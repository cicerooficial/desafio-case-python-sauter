'''
  Tarefa 3 Projeto: Desafio: Capturar dados de Loja de Aplicativo - Google Play
  Autor: Cícero Henrique dos Santos
  Descrição: Criar objeto com operações de captura de dados, com atualização da tabela. O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews. 

'''

'''
ATENÇÃO!

Antes de executar o arquivo, você precisa definir uma variável de ambiente em que seu código é executado.
1. Crie uma conta de serviço - https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account
2. Forneça credenciais de autenticação ao código do aplicativo definindo a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS.
- Veja mais em: Como configurar a variável de ambiente para autenticação: https://cloud.google.com/docs/authentication/getting-started#windows
3. Crie uma chave de conta de serviço por meio da página de criação de chave de conta de serviço no console do Google Cloud Platform - https://console.cloud.google.com/apis/credentials/serviceaccountkey.
Selecione o projeto> clique na aba Chaves > tipo de chave JSON e baixe o arquivo de chave.
4. Para evitar alguns conflitos, instale o gerenciador de pacotes PIP para 
### Windows ###
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py # Baixar diretório do pip
python get-pip.py                                       # Instalar o pip
python -m pip install --upgrade pip #Instalar o PIP     # Atualizar o pip
py -m pip freeze > requirements.txt                     # Um jeito simples de criar o seu próprio arquivo de depências
py -m pip install -r requirements.txt                   # Instalar dependências

Linux
sudo apt update
sudo apt install python3-pip
sudo pip3 install --upgrade pip
python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt

'''

from google.cloud import client, storage
from google.oauth2 import service_account
import pandas as pd

my_bucket_name  = 'bigquery-gcp-scrapper'
my_project      = 'bigquery-google-play-scrapper'
my_project_id   = 'nifty-foundry-336623'
SCOPE = ["https://www.googleapis.com/auth/cloud-platform"]


class etl_with_gcp():
 
    #Classe de construtores para sempre iniciar por esta antes das demais e subir as chaves
    def __init__(self):
        self.my_credential = service_account.Credentials.from_service_account_file('C:/Users/cicer/Documents/GitHub/desafio-case-python-sauter/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json', scopes=SCOPE)
        self.client = storage.Client.from_service_account_json('C:/Users/cicer/Documents/GitHub/desafio-case-python-sauter/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json')   # Acesso ao Google Cloud Storage 

    #Função para capturar(extrair) dados no google play e enviar dados em arquivos csv para o Google Cloud Storage
    
    def scraper_google_play(self):
        try:
            # Ajustar código da tarefa 1 para capturar os dados e jogar no Cloud Storage
            print('Sucesso! Captura de dados realizada')
        except:
            print('Erro! Não foi possível realizar a captura de dados')

    #Função para fazer download dos arquivos CSV do Google Cloud Storage
    def download_files_csv_cloud_storage(self):

        try:
            bucket = self.client.bucket(my_bucket_name)
            blobs = self.client.list_blobs(my_bucket_name)                                # Armazenar arquivos em uma lista     
            
            # Laço para percorrer cada elemento de dentro do bucket
            for object in blobs:
                arquivo = bucket.blob(object.name)          # Captura o nome do arquivo de acordo com a posição do laço
                arquivo.download_to_filename(object.name)   # Salva o arquivo com o mesmo nome
                print(arquivo)
            print('Sucesso! Download de arquivos CSV completados')
        except:
            print('Erro! Download imcompleto, algo deu errado.')

    # Função para enviar Dataframes para o DataWarehouse(BigQuery) 
    def upload_dataframe_to_bigquery(self):

        #Lê os arquivos CSVs e armazena os dados em um DataFrame
        df_aval_positiva    = pd.read_csv('aval_positiva.csv', sep=';')
        df_aval_neutra      = pd.read_csv('aval_neutra.csv', sep=';')
        df_aval_negativa    = pd.read_csv('aval_negativa.csv', sep=';')

        try: 
            # Carregar DataFrames para tabela dentro do Datawarehouse(Bigquery)
            df_aval_positiva.to_gbq(
                destination_table='avaliacao_positiva.avaliacao_positiva', 
                project_id=my_project_id, 
                if_exists='replace', 
                credentials=self.my_credential)
            print('Sucesso! df_aval_positiva enviado para o BigQuery')

            df_aval_neutra.to_gbq(
                destination_table='avaliacao_neutra.avaliacao_neutra', 
                project_id=my_project_id, 
                if_exists='replace', 
                credentials=self.my_credential)
            print('Sucesso! df_aval_neutra enviado para o BigQuery')

            df_aval_negativa.to_gbq(
                destination_table='avaliacao_negativa.avaliacao_negativa', 
                project_id=my_project_id, 
                if_exists='replace', 
                credentials=self.my_credential)
            print('Sucesso! df_aval_negativa enviado para o BigQuery')
        except:
            print('Erro! Não foi possível enviar arquivos para o BigQuery')



if __name__ == "__main__":
    #etl_with_gcp().scraper_google_play()
    etl_with_gcp().download_files_csv_cloud_storage()
    etl_with_gcp().upload_dataframe_to_bigquery()
