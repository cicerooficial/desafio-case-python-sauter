<center>

![Logo Sauter](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/logo_sauter.png)

</center>

# Desafio Sauter: Capturar dados de Loja de Aplicativo - Google Play

<p align="center">
    <img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"/>
	<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
	<img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white"/>

</p>

- Autor: Cícero Henrique dos Santos
- E-mail: cicerooficial@gmail.com
- Linkedin: https://www.linkedin.com/in/cicero-henrique-santos/

------

## 📌 Tópicos:
- [Descrição do projeto](#descrição-do-projeto)
- [Objetivos](#objetivos)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar a aplicação](#como-rodar-a-aplicação)
- [Tarefas em aberto](#tarefas-em-aberto)
- [Linguagens, dependencias e libs utilizadas](#linguagens-dependencias-e-libs-utilizadas)
- [Referências](#referências)

------

## 📝 Descrição do projeto
O Desafio Python tem como objetivo refletir alguns desafios que um Engenheiro de Dados possa enfrentar na [Sauter](https://sauter.digital/).

⚠ É importante saber que há múltiplos formatos para a resolução do desafio e será necessário consultar documentações (algumas das quais estão identificadas abaixo).

------

## 🎯 Objetivos

### ✅ Tarefa 1: 
Sua primeira tarefa é utilizar a library google-play-scraper para capturar dados de apps.
O app selecionado é o [Alexa](https://play.google.com/store/apps/details?id=com.amazon.dee.app), da Amazon.

1. Utilizando as informações de avaliação do aplicativo, você deve chegar em um Data Frame de review parecido com o demonstrado abaixo:

![DataFrame_Example](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/df_example.png)

A partir desse Data Frame, seguem as atividades propostas na tarefa:

2.  Criar 3 arquivos .csv a partir do dataframe, com a seguinte classificação:
    1. aval_positiva.csv para score maior ou igual a 4; 
    2. aval_neutra.csv para score igual a 3;
    3. aval_negativa.csv para score inferior a 3.

3.  Criar um report simples para essas variáveis utilizando a library [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html) para cada uma das separações (aval_neutra, aval_positiva, aval_negativa). </br>
⚠ É importante notar os principais pontos de cada análise para sua apresentação.</br>
Finalmente, salvar o resultado do profile em formato .html.

### ✅ Tarefa 2: 
1. A partir dos dados criados, subir as tabelas para um banco de dados.
 Aqui é completamente opcional qual banco de dados utilizar, mas considerar utilizar o [BigQuery](https://cloud.google.com/bigquery/docs/tables) da Google, pois é totalmente gratuito (para o tamanho do dataset) e em cloud.

    ⚠ Caso prefira utilizar outro banco de dados de seu domínio também vale como problema resolvido.

### ✅ Tarefa 3: 
1. Criar objeto com operações de captura de dados, com atualização da tabela. O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews.

#### Design de pipeline proposto com Airflow:    
![Design Pipeline Airflow](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/design_pipeline_airflow.png)

------

## ❗ Pré-requisitos

Para a Tarefa 3, configure o docker em sua máquina seguindo os passos abaixo:

## Configurando o Docker em sua máquina:

A fim de facilitar o desenvolvimento das etapas do projeto, abaixo segue um passo a passo de preparação de ambiente.

### Download Docker e Docker Compose:

### Download Docker - Windows

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação Docker - Windows

1. Verificar se o Windows está atualizado. Caso seja inferiro a 18362, clique no link ao lado para atualizar o Windows 10. [Atualizar o Windows](https://www.microsoft.com/pt-br/software-download/windows10);
2. Pesquise por Ativar ou desativar recursos do Windows e siga os passos abaixo:
    - Desativar Hyper-V;
    - Desativar Plataforma do Hipervisor do Windows;
    - Habilitar a Plataforma de Máquina Virtual;
    - Habilitar o Subsistema do Windows para Linux (WSL).
3. Faça o Download do WSL 2 clicando no link ao lado: [Download WSL 2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi);
4. Acesse a Microsoft Store, e faça download e instale a distribuição Linux Ubuntu 20.04 LTS (recomendado);
5. Instale o Docker Desktop no Windows: [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows);
    - Obs: Abra o Docker Desktop e verifique se estão habilitados o "Enable integration with my default WSL distro" e "Ubuntu-20.04" em Settings->Resource->WSL Integration.

### Instalação Docker - Linux

- [Link para instalação do Docker Engine](https://docs.docker.com/engine/install/)
- [Link para instalação do Docker Compose](https://docs.docker.com/compose/install/)

### Instalação Docker - Mac
- [Link para instalação do Docker Desktop no Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)

------

## 🔄 Como rodar a aplicação

- Tarefa 1 - Capturar dados de Loja de Aplicativo - Google Play
    1. Acessar o Google Colab: https://colab.research.google.com/drive/1ak9TAlvzWBj5Hh39swM8iG-uF1dVaDe6?usp=sharing;
    2. Acessar diretamente o arquivo no diretório: 
    [Google Colab - Capturando dados com Google-Play-Scraper](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb)
    - [Pasta com arquivos CSV](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/csv)
    - [Pasta com reports em html](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/reports)
    
- Tarefa 2 - Subir as tabelas para um BD
    1. Acesse o arquivo com o passo: [Armazenar dados no BigQuery](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/Armazenar_dados_no_BigQuery.md)

- Tarefa 3 - Criar Pipeline de dados
    1. Acesse a pasta dags para mais informações sobre o desenvolvimento da tarefa 3 e arquivos: [Pasta dags](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/dags)

![Painel Pipeline OK 1 ](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/pipeline_ok_2.png)
![Painel Pipeline OK 2](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/pipeline_ok.png)

    1. Abra o terminal do WSL2 e crie um diretório para o projeto no `~$/home/<seu-nome>` com o comando: `mkdir apache-airflow`;
    2. Acesse o diretório `cd apache-airflow`;
    3. No diretório apache-airflow, baixe o arquivo `docker-compose.yaml` disponibilizado na documentação oficial: `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'`;
    4. Confirme se o arquivo foi baixado com o comando de listar: `ls`;
    5. No Linux , o início rápido precisa saber a id do usuário do host e precisa ter a id do grupo definida como 0. Caso contrário, os arquivos criados no dags, logse pluginsserá criado com rootusuário. Você deve certificar-se de configurá-los para o docker-compose:
     `mkdir -p ./dags ./logs ./plugins` | `echo -e "AIRFLOW_UID=$(id -u)" > .env`;
    6. Em todos os sistemas operacionais , você precisa executar migrações de banco de dados e criar a primeira conta de usuário. Para fazer isso, execute:
    `docker-compose up airflow-init`;
    7. Inicie todos os serviços: `docker-compose up -d`;
    ![Instalação Airflow Terminal](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/airflow1.png)
    8. Acesse o servidor web do Airflow disponível em: http://localhost:8080. A conta padrão possui o login **airflowe** a senha **airflow**.
    ![Acesso ao Apache Airflow](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/airflow2.png)
    
------
## 📝 Tarefas em aberto

✅ 1. No Google Colab, enviar dados CSV para o BigQuery via Python; 

✅ 2. Criar função Python para:
    - Extrair dados do app no Google Play;
    - Enviar dados para o Google Cloud Storage;
    - Baixar CSVs do Cloud Storage e tranformar em Dataframe
    - Caregar datafranmes em uma tabela no DataWarehouse(BigQuery).

✅ 3. Criar pipeline da função acima via Airflow através de DAGs.

⬜ 4. Criar exemplo de Deploy do pipeline via Airflow.

⬜ 5. Corrigir erro de dependencia google-play-scraper da função scraper_google_play(self) para realizar ETL completo;

------
## 🗃 Linguagens, dependencias e libs utilizadas

|Lang/Lib/Framwork             |Version          |
|------------------------------|-----------------|
|Python                        |3.8              |
|google-play-scraper           |v1.0.2           |
|pandas                        |v1.3.5           |
|pandas-profiling              |v3.1.0           |
|pandas_gbq                    |v0.15.0          |
|Docker                        |v4.3.2           |
|Docker Compose                |v1.29.2          |
|Apache Airflow                |v2.0.2           |
|google-cloud-storage          |v1.43.0          |
|pip                           |v21.3.1          |
|Google Colab                  |                 |
|Google Cloud Storage (GCS)    |                 |
|Google BigQuery (GBQ)         |                 |


------
## 📚 Referências

- [Documentação google-play-scraper 1.0.2](https://pypi.org/project/google-play-scraper/)
- [Documentação Pandas API reference](https://pandas.pydata.org/docs/reference/)
- [Documentação Package pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
- [Como criar um projeto no GCP](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br&visit_id=637763797785493881-2801279509&rd=1#creating_a_project)
- [Como criar buckets de armazenamento](https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-gsutil)
- [Como criar um conjunto de dados](https://cloud.google.com/bigquery/docs/datasets#create-dataset)
- [Como carregar dados CSV em uma tabela BigQuery](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table)
- [ETL com Airflow, Google Cloud Storage e BigQuery](https://github.com/okzapradhana/etl-flatfile-airflow#etl-with-airflow-google-cloud-storage-and-bigquery)
- [Executando o Airflow no Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
- [Google Cloud Client Libraries for google-cloud-storage](https://googleapis.dev/python/storage/latest/index.html)
- [Google Auth Library for Python](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html)
- [Documentação pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)
- [Como fazer o download de objetos](https://cloud.google.com/storage/docs/downloading-objects#storage-download-object-python)
- [Como fazer upload de objetos](https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample)
- [Como configurar a variável de ambiente para autenticação](https://cloud.google.com/docs/authentication/getting-started#windows)
- [Autenticação com pandas-bq](https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html)
- [Módulo de autenticação google-auth](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html)
- [Documentation pip v21.3.1](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
- [Documentação Apache Airflow Exemplo de Pipeline](https://airflow.apache.org/docs/apache-airflow/1.10.1/tutorial.html#example-pipeline-definition)

------
## 📎 Conclusão

