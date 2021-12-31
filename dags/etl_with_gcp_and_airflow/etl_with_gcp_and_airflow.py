'''
  Tarefa 3 Projeto: Desafio: Capturar dados de Loja de Aplicativo - Google Play
  Autor: Cícero Henrique dos Santos
  Descrição: Criar objeto com operações de captura de dados, com atualização da tabela. 
  O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews. 

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
from    google.cloud           import   client, storage     # Importa métodos de acesso ao Google Cloud Storage
from    google.oauth2          import   service_account     # Importa métodos de autenticação da conta de serviço do Google Cloud
from    google_play_scraper    import   Sort, reviews_all   # Importa métodos Sort e reviews para buscar avaliações do aplicativo pela biblioteca google_play_scraper
import  pandas                 as       pd                  # Importa biblioteca pandas para analise de dados

my_bucket_name  = 'bigquery-gcp-scrapper'
my_project      = 'bigquery-google-play-scrapper'
my_project_id   = 'nifty-foundry-336623'
SCOPE           = ["https://www.googleapis.com/auth/cloud-platform"]


class etl_with_gcp():
 
    #Classe de construtores para sempre iniciar por esta antes das demais e subir as chaves
    def __init__(self):
        #PARA TESTE NO WINDOWS
        #self.my_credential = service_account.Credentials.from_service_account_file('C:/Users/cicer/Documents/GitHub/desafio-case-python-sauter/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json', scopes=SCOPE)
        #self.client = storage.Client.from_service_account_json('C:/Users/cicer/Documents/GitHub/desafio-case-python-sauter/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json')   # Acesso ao Google Cloud Storage 
        self.my_credential = service_account.Credentials.from_service_account_file('/opt/airflow/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json', scopes=SCOPE)
        self.client = storage.Client.from_service_account_json('/opt/airflow/dags/etl_with_gcp_and_airflow/nifty-foundry-336623-dad5e810d66e.json')   # Acesso ao Google Cloud Storage 

    #Função para capturar(extrair) dados no google play e enviar dados em arquivos csv para o Google Cloud Storage
    
    def scraper_google_play(self):
        try:
            app_id = 'com.amazon.dee.app'         # Armazena o ID do App   
            resultado_revisao = []                # Criar lista para armazenar os resultados capturados

            # Criando uma lista com os resultados das análises do app rastreados 
            for pontuacao in list(range(1, 6)):   # Laço para percorrer as avaliações por nível de classificação de 1 a 5
                resultado = reviews_all(
                    app_id,                         # Busca os dados do app Alexa
                    sleep_milliseconds=0,           # Define limite em 0 milisegundos para rastrear
                    lang='pt',                      # Define linguagem como família português
                    country='br',                   # Define a região de origem como Brasil
                    sort=Sort.RATING,               # Pesquisa por avaliação (RATING)
                    filter_score_with = pontuacao,  # Definindo o filtro de acordo com a potuação atual do for 
            )
            resultado_revisao.extend(resultado) # Salva cada captura dentro da última posição da lista

            df_alexa = pd.DataFrame(resultado_revisao)  # Salvando a lista de resultado em um DataFrame com pandas
            
            print('Sucesso! Captura de dados realizada')
            
            # Filtrando colunas selecionadas com o método filter
            df_alexa = df_alexa.filter(['content', 'score',	'thumbsUpCount', 'reviewCreatedVersion', 'at'])

            df_aval_positiva    = df_alexa.loc[df_alexa['score'] >= 4] # Classificação positiva (maior ou igual a 4)
            df_aval_neutra      = df_alexa.loc[df_alexa['score'] == 3] # Classificação neutra (Igual a 3)
            df_aval_negativa    = df_alexa.loc[df_alexa['score'] < 3]  # Classificação negativa (Menor que 3)

            # Salvar classificação positiva em arquivo CSV
            df_aval_positiva.to_csv('aval_positiva.csv',  # Definie o nome do arquivo
                                    encoding='utf-8',         # Definie a codificação para utf-8
                                    index=False,          # Define a retirada do index
                                    sep=';',              # Define o separador como ';'
                                    header=True           # Define salvar como cabeçalho
            )
            # Salvar classificação neutra em arquivo CSV
            df_aval_neutra.to_csv('aval_neutra.csv',   # Definie o nome do arquivo
                                encoding='utf-8',  # Definie a codificação para utf-8
                                index=False,       # Define a retirada do index
                                sep=';',           # Define o separador como ';'
                                header=True        # Define salvar como cabeçalho
            )
            # Salvar classificação neutra em arquivo CSV
            df_aval_negativa.to_csv('aval_negativa.csv',  # Definie o nome do arquivo
                                encoding='utf-8',     # Definie a codificação para utf-8
                                index=False,          # Define a retirada do index
                                sep=';',              # Define o separador como ';'
                                header=True           # Define salvar como cabeçalho
            )
            
            print('Sucesso! Arquivos CSVs salvos')
            
            # Envio de arquivos para o Google Cloud Storage
            bucket = self.client.bucket(my_bucket_name)                 # Define o nome do Bucket
            blob = bucket.blob('aval_positiva.csv')                     # Define o local onde o arquivo será armazenado
            blob.upload_from_filename('aval_positiva.csv')              # Define o nome que o arquivo será armazenado

            bucket = self.client.bucket(my_bucket_name)                 # Define o nome do Bucket
            blob = bucket.blob('aval_neutra.csv')                       # Define o local onde o arquivo será armazenado
            blob.upload_from_filename('aval_neutra.csv')                # Define o nome que o arquivo será armazenado

            bucket = self.client.bucket(my_bucket_name)                 # Define o nome do Bucket
            blob = bucket.blob('aval_negativa.csv')                     # Define o local onde o arquivo será armazenado
            blob.upload_from_filename('aval_negativa.csv')              # Define o nome que o arquivo será armazenado
            
            print('Sucesso! Arquivos enviados para o Google Cloud Storage')

        except:
            print('Erro! Não foi possível realizar a captura de dados')

    #Função para fazer download dos arquivos CSV do Google Cloud Storage
    def download_files_csv_cloud_storage(self):

        try:
            bucket = self.client.bucket(my_bucket_name)                             # Define o nome do Bucket
            blobs = self.client.list_blobs(my_bucket_name)                          # Armazenar arquivos em uma lista passando o nome do bucket de onde estão os arquivos
            
            # Laço para percorrer cada elemento de dentro do bucket
            for object in blobs:
                arquivo = bucket.blob(object.name)                                  # Captura o nome do arquivo de acordo com a posição do laço
                arquivo.download_to_filename(object.name)                           # Salva o arquivo com o mesmo nome
                print(arquivo)                                                      # Imprime o nome do arquivo que foi realizado o download a cada laço
            print('Sucesso! Download de arquivos CSV completados')
        except:
            print('Erro! Download imcompleto, algo deu errado.')

    # Função para enviar Dataframes para o DataWarehouse(BigQuery) 
    def upload_dataframe_to_bigquery(self):

        #Lê os arquivos CSVs e armazena os dados em um DataFrame
        df_aval_positiva    = pd.read_csv('aval_positiva.csv',  sep=';')             # Armazena os dados do CSV aval_positiva.csv no DataFrame df_aval_positiva
        df_aval_neutra      = pd.read_csv('aval_neutra.csv',    sep=';')             # Armazena os dados do CSV aval_neutra.csv no DataFrame df_aval_neutra
        df_aval_negativa    = pd.read_csv('aval_negativa.csv',  sep=';')             # Armazena os dados do CSV aval_negativa.csv no DataFrame df_aval_negativa

        try: 
            # Carregar DataFrames para tabela dentro do Datawarehouse(Bigquery)
            df_aval_positiva.to_gbq(
                destination_table   =   'avaliacoes.avaliacao_positiva',    # Define o caminho da tabela de destino criada no BigQuery = NomeConjuntodeDados.nomedaTabela
                project_id          =   my_project_id,                              # Define o nome do ID do projeto 
                if_exists           =   'replace',                                  # Substitui a tabela caso já exista, a fim de evitar dados duplicados na mesma tabela 
                credentials         =   self.my_credential                          # Define a credencial de serviço de acesso 
            )                         
            print('Sucesso! df_aval_positiva enviado para o BigQuery')

            df_aval_neutra.to_gbq(
                destination_table   =   'avaliacoes.avaliacao_neutra',        # Define o caminho da tabela de destino criada no BigQuery = NomeConjuntodeDados.nomedaTabela
                project_id          =   my_project_id,                              # Define o nome do ID do projeto 
                if_exists           =   'replace',                                  # Substitui a tabela caso já exista, a fim de evitar dados duplicados na mesma tabela
                credentials         =   self.my_credential                          # Define a credencial de serviço de acesso 
            )
            print('Sucesso! df_aval_neutra enviado para o BigQuery')

            df_aval_negativa.to_gbq(
                destination_table   =   'avaliacoes.avaliacao_negativa',    # Define o caminho da tabela de destino criada no BigQuery = NomeConjuntodeDados.nomedaTabela
                project_id          =   my_project_id,                              # Define o nome do ID do projeto 
                if_exists           =   'replace',                                  # Substitui a tabela caso já exista, a fim de evitar dados duplicados na mesma tabela
                credentials         =   self.my_credential                          # Define a credencial de serviço de acesso 
            )
            print('Sucesso! df_aval_negativa enviado para o BigQuery')
        except:
            print('Erro! Não foi possível enviar arquivos para o BigQuery')

# Testar funções separadamente
#if __name__ == "__main__":
    #etl_with_gcp().scraper_google_play()
    #etl_with_gcp().download_files_csv_cloud_storage()
    #etl_with_gcp().upload_dataframe_to_bigquery()