
<center>

![Logo Sauter](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/logo_sauter.png)

</center>

# Desafio: Capturar dados de Loja de Aplicativo - Google Play

## Tópicos:
- [Descrição do projeto](#descrição-do-projeto)
- [Objetivos](#objetivos)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar a aplicação](#como-rodar-a-aplicação)
- [Linguagens, dependencias e libs utilizadas](#linguagens-dependencias-e-libs-utilizadas)
- [Referências](#referências)

------

## Descrição do projeto
O Desafio Python tem como objetivo reflitir alguns desafios que um Engenheiro de Dados possa enfrentar na [Sauter](https://sauter.digital/).

⚠ É importante saber que há múltiplos formatos para a resolução do desafio e será necessário consultar documentações (algumas das quais colocaremos o link aqui).

------

## Objetivos

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
- [Pasta com arquivos CSV](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/csv)

3.  Criar um report simples para essas variáveis utilizando a library [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html) para cada uma das separações (aval_neutra, aval_positiva, aval_negativa). </br>
⚠ É importante notar os principais pontos de cada análise para sua apresentação.</br>
Finalmente, salvar o resultado do profile em formato .html.
- [Pasta com reports em html](https://github.com/cicerooficial/desafio-case-python-sauter/tree/main/reports)

### ✅ Tarefa 2: 
1. A partir dos dados criados, subir as tabelas para um banco de dados.
 Aqui é completamente opcional qual banco de dados utilizar, mas considerar utilizar o [BigQuery](https://cloud.google.com/bigquery/docs/tables) da Google, pois é totalmente gratuito (para o tamanho do dataset) e em cloud.

    ⚠ Caso prefira utilizar outro banco de dados de seu domínio também vale como problema resolvido.

### ⬜ Tarefa 3: 
1. Criar objeto com operações de captura de dados, com atualização da tabela. O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews.

------

## Pré-requisitos


------

## Como rodar a aplicação

Tarefa 1 - Capturar dados de Loja de Aplicativo - Google Play
1. Acessar o Google Colab: https://colab.research.google.com/drive/1ak9TAlvzWBj5Hh39swM8iG-uF1dVaDe6?usp=sharing;
2. Acessar o diretótio do arquivo baixado: 
[Google Colab - Capturando dados com Google-Play-Scraper](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb)

Tarefa 2 - Subir as tabelas para um BD
1. Acesse o arquivo com o passo: [Armazenar dados no BigQuery](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/Armazenar_dados_no_BigQuery.md)

Tarefa 3 - Criar Pipeline de dados

------

## Linguagens, dependencias e libs utilizadas

|Lang/Lib/Framwork    |Version          |
|---------------------|---------        |
|Python               |3.8              |
|Google-Play-Scraper  |v1.0.2           |
|Pandas               |v1.3.5           |
|Pandas Profiling     |v3.1.0           |

------
## Referências

- [Documentação google-play-scraper 1.0.2](https://pypi.org/project/google-play-scraper/)
- [Documentação Pandas API reference](https://pandas.pydata.org/docs/reference/)
- [Documentação Package pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
- [Como criar um projeto no GCP](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br&visit_id=637763797785493881-2801279509&rd=1#creating_a_project)
- [Como criar buckets de armazenamento](https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-gsutil)
- [Como criar um conjunto de dados](https://cloud.google.com/bigquery/docs/datasets#create-dataset)
- [Como carregar dados CSV em uma tabela](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table)