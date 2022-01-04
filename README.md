<center>

![Logo Sauter](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/logo_sauter.png)

</center>

# Desafio Sauter: Capturar dados de Loja de Aplicativo - Google Play

<p align="center">
    <img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20CONCLUÍDO&color=RED&style=for-the-badge"/>
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
- [Descrição do projeto](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Objetivos](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Pré-requisitos](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Como rodar a aplicação](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Tarefas em aberto](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Linguagens, dependencias e libs utilizadas](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Referências](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)
- [Conclusão](https://github.com/cicerooficial/desafio-case-python-sauter#descri%C3%A7%C3%A3o-do-projeto)

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

### Tarefa 1
 Para realização da Tarefa 1 utilize alguma plataforma notebook de sua preferência.

Exemplo: 
[Google Colab](https://colab.research.google.com/?hl=pt-BR&skip_cache=false%22)
[Jupiter Notebook](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/HEAD?urlpath=lab/tree/demo)

Entre outros...

### Tarefa 2
Para realização da Tarefa 2 é possível realizar de forma manual pela plataforma do [Google CLoud Platform](https://cloud.google.com/free) ou através de comandos no próprio Google Colab ou Jupiter Notebook. 

### Tarefa 3
Para a Tarefa 3, configure o docker em sua máquina (no caso utilizei Windows) seguindo os passos abaixo:

### Configurando o Docker em sua máquina:

#### Download Docker: [Docker](https://docs.docker.com/get-docker/)
#### Download Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/)


#### Instalação Docker - Windows

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

#### Instalação do Apache Airflow no Docker
- Documentação - [Executando o Airflow no Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
- Abra o terminal do WSL2 e crie um diretório para o projeto no ***home/<seu-diretório>*** com o comando: `mkdir apache-airflow`;
- Acesse o diretório `cd apache-airflow`;
- No diretório apache-airflow, baixe o arquivo `docker-compose.yaml` disponibilizado na documentação oficial através do comando: `curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'`;
- Confirme se o arquivo foi baixado com o comando de listar: `ls`;
- No Linux , o início rápido precisa saber a id do usuário do host e precisa ter a id do grupo definida como 0. Caso contrário, os arquivos criados no dags, logs e plugins serão criados com usuário root. Você deve certificar-se de configurá-los para o docker-compose:
    `mkdir -p ./dags ./logs ./plugins` | `echo -e "AIRFLOW_UID=$(id -u)" > .env`;
- Em todos os sistemas operacionais, você precisa executar migrações de banco de dados e criar a primeira conta de usuário. Para fazer isso, execute:
`docker-compose up airflow-init`;
- Inicie todos os serviços através do comando: `docker-compose up -d`;
![Instalação Airflow Terminal](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/airflow1.png)
- Acesse o servidor web do Apache Airflow disponível em: http://localhost:8080. A conta padrão possui o login **airflow** e a senha **airflow**.
![Acesso ao Apache Airflow](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/airflow2.png)

------

## 🔄 Como rodar a aplicação

- Tarefa 1 - Capturar dados de Loja de Aplicativo - Google Play
    1. Acessar o Google Colab: https://colab.research.google.com/drive/1ak9TAlvzWBj5Hh39swM8iG-uF1dVaDe6?usp=sharing;
    2. Acessar diretamente o arquivo no diretório: 
    [Google Colab - Capturando dados com Google-Play-Scraper](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb)
    - [Pasta com arquivos CSV](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/csv);
    - [Pasta com reports em html](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/reports).
    
- Tarefa 2 - Subir as tabelas para um BD
    1. Acesse o arquivo com o passo a passo manual: [Armazenar dados no BigQuery](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/Armazenar_dados_no_BigQuery.md);
    2. Siga os passos dentro do Google Colab [Google Colab - Capturando dados com Google-Play-Scraper](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb) no tópico **Enviar dados CSV para bucket no Cloud Storage e Big Query**.

- Tarefa 3 - Criar Pipeline de dados
    1. Transfira os arquivos do pipeline da [Pasta dags](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/dags) para a pasta dags do Airflow (esta pasta foi criada no momento da instalação juntamente com as pastas logs e plugins no último passo do tópico **Instalação do Apache Airflow no Docker**). Utilize o comando `cp /mnt/c/Users/<caminho onde até a pasta desafio-case-python-sauter>/dags /home/<seu diretório>/apache airflow/`;
    1. Acesso o arquivo etl_with_gcp_and_airflow.py dentro da pasta dags/etl_with_gcp_and_airflow. Dentro do arquivo, na funçao `def __init__(self)` comente as linhas com o caminho para teste WINDOWS e descomente as linhas de teste para LINUX
    1. A fim de evitar conflitos por falta de dependências, execute o arquivo shell dentro da pasta ***\dags\etl_with_gcp_and_airflow***: 
        - Dentro da pasta mencionada, acesso o arquivo através do de um editor de texto de sua oreferência (no caso utilizei o NANO). Através do comando `nano pip_install_requirements.sh` desabilite os comentários de acordo com seu sistema operacional. Salve com o comando `CTRL + O` e depois feche o editor de texto com o comando `CTRL + X`;
        ![Instalação pip e requirements.txt](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/instalacao_pip_requirements.png)
        - Agora (no WSL/Linux) execute o script através do comando `sh pip_install_requirements.sh`.
    1. Crie uma conta se serviço para autenticação de acesso ao Google Cloud seguindo os passos através do link: [Como criar uma conta de serviço](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account) e salve o arquivo dentro da pasta \dags\etl_with_gcp_and_airflow;
    1. Com as configurações necessárias realizadas, (caso não esteja com o Apache Airflow iniciado) execute o comando `docker-compose up -d` dentro do diretório onde o arquivo se encontra: ***/home/<seu diretório>/apache airflow***;
    1. Acesse o servidor web do Apache Airflow disponível em: http://localhost:8080. A conta padrão possui o login **airflow** e a senha **airflow**;
    1. Dentro do Apache Airflow, na aba DAGs, procure pelo DAG **pipeline_etl_with_gcp_and_airflow** e execute para certificar que tudo está funcionando corretamente. Por padrão as sinalizações de execução devem conter o status com a cor verde, indicando  **sucess** na execução.
        - Abaixo segue os prints de demonstração das Dags com status de Sucess: 
        - Pipeline completo no Airflow:
        ![Painel Pipeline OK 1 ](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/pipeline_ok_2.png)
        ![Painel Pipeline OK 2](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/pipeline_ok.png)        
    

------
## 📝 Tarefas em aberto

⬜ 1. Criar exemplo de Deploy do pipeline via Airflow.

------
## 🗃 Linguagens, dependencias e libs utilizadas

|Lang/Lib/Framwork             |Version          |
|------------------------------|-----------------|
|Python                        |3.10             |
|google-play-scraper           |1.0.2            |
|pandas                        |1.3.5            |
|pandas-profiling              |3.1.0            |
|pandas_gbq                    |0.15.0           |
|Docker                        |4.3.2            |
|Docker Compose                |1.29.2           |
|Apache Airflow                |2.0.2            |
|google-cloud-storage          |1.43.0           |
|pip                           |21.3.1           |
|Google Cloud Storage (GCS)    |                 |
|Google BigQuery (GBQ)         |                 |
|Google Colab                  |                 |
|Visual Studio Code            |                 |

------
## 📚 Referências

- [Documentação google-play-scraper 1.0.2](https://pypi.org/project/google-play-scraper/)
- [Documentação Pandas API reference](https://pandas.pydata.org/docs/reference/)
- [Documentação Package pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
- [Como criar um projeto no GCP](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br&visit_id=637763797785493881-2801279509&rd=1#creating_a_project)
- [Como criar buckets de armazenamento](https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-gsutil)
- [Como criar um conjunto de dados](https://cloud.google.com/bigquery/docs/datasets#create-dataset)
- [Como carregar dados CSV em uma tabela BigQuery](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table)
- [Executando o Airflow no Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
- [ETL com Airflow, Google Cloud Storage e BigQuery](https://github.com/okzapradhana/etl-flatfile-airflow#etl-with-airflow-google-cloud-storage-and-bigquery)
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
- [Módulos de providers do google disponíveis](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/index.html)

------

## 📎 Conclusão
Com o desenvolvido do projeto foi possível obter maiores conhecimentos de libs que facilitam o trabalho de ETL (Extração, Transformação e Carregamento) para o dia a dia de um Engenheiro de Dados, como:

1. Utilizar a lib google-plat-scraper em vez da comumente usada beautifulsoup; 
2. um diferencial foi conhecer a lib pandas-profiling, com acesso a funções de análise de dados de forma rápida e bem completa para usos mais comuns, encurtando o processo de construção de scripts para cada tipo de análise;
3. Utilizar o Google Coud Storage em formato de comandos, já que através do qwiklabs é demonstrado em formato manual em sua forma normal;
4. Um dos maiores desafios dentre os 3 foi buscar informações sobre como construir as DAGs no Apache Airflow. Sua documentação principal é mais limitada, mas após encontrar a documentação com [exemplos de Pipeline](https://airflow.apache.org/docs/apache-airflow/1.10.1/tutorial.html#example-pipeline-definition), foi possível ter uma maior clareza e rapidez em montar as Tasks e DAGs. 

Por fim, o desafio foi uma ótima oportunidade de auto desafio, confiança em desenvolver um projeto "real" utilizando tantas stacks diferentes e construção de um projeto que servirá também como portifólio.
  
Aprendizados:

A maior dificuldade foi em tentar resolver o erro de *módulo google-play-scraper* não identificado no Apache Airflow. 

Busquei desenvolver o pipeline completo seguindo o script etl_with_gcp_and_airflow.py, mas, devido o Apache Airflow ainda não possuir dentro de seu repositório de providers do Google suporte ao módulo do google-play-scrapper (conforme a documentação [Módulos de providers do google disponíveis](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/index.html)), não foi possível realizar o pipeline com a função de capturar os dados, somente as funções de download dos CSVs do Cloud Storage e envio ao Big Query foi possível realizar (Conforme solicitado no objetivo de tarefa 3).

Caso deseje executar o script completo, descomente as últimas linhas do arquivo da função main, execute os comandos para evitar erros de dependências ao executar o script.