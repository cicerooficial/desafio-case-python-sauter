
<center>

![Logo Sauter](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/logo_sauter.png)

</center>

# Desafio: Capturar dados de Loja de Aplicativo - Google Play

## Tópicos:
- [Descrição do projeto](#descrição-do-projeto)
- [Objetivos](#objetivos)
- [Deploy da Aplicação](#deploy-da-aplicação)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar a aplicação](#como-rodar-a-aplicação)
- [Linguagens, dependencias e libs utilizadas](#linguagens-dependencias-e-libs-utilizadas)
- [Tarefas em aberto](#tarefas-em-aberto)

------

## Descrição do projeto
O Desafio Python tem como objetivo reflitir alguns desafios que um Engenheiro de Dados possa enfrentar na [Sauter](https://sauter.digital/).

⚠ É importante saber que há múltiplos formatos para a resolução do desafio e será necessário consultar documentações (algumas das quais colocaremos o link aqui).

------

## Objetivos

### Tarefa 1: 
Sua primeira tarefa é utilizar a library google-play-scraper para capturar dados de apps.
O app selecionado é o [Alexa](https://play.google.com/store/apps/details?id=com.amazon.dee.app), da Amazon.

1. ✅ Utilizando as informações de avaliação do aplicativo, você deve chegar em um Data Frame de review parecido com o demonstrado abaixo:

![DataFrame_Example](https://raw.githubusercontent.com/cicerooficial/desafio-case-python-sauter/main/img/df_example.png)

A partir desse Data Frame, seguem as atividades propostas na tarefa:

2.  ✅ Criar 3 arquivos .csv a partir do dataframe, com a seguinte classificação:
    1. aval_positiva.csv para score maior ou igual a 4; 
    2. aval_neutra.csv para score igual a 3;
    3. aval_negativa.csv para score inferior a 3.

3.  ✅ Criar um report simples para essas variáveis utilizando a library pandas profiling para
cada uma das separações (aval_neutra, aval_positiva, aval_negativa). </br>
⚠ É importante notar os principais pontos de cada análise para sua apresentação.</br>
Finalmente, salvar o resultado do profile em formato .html.

[Google Colab - Capturando dados com Google-Play-Scraper](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb)

### Tarefa 2: 
1. ✅ A partir dos dados criados, subir as tabelas para um banco de dados.
 Aqui é completamente opcional qual banco de dados utilizar, mas considerar utilizar o [BigQuery](https://cloud.google.com/bigquery/docs/tables) da Google, pois é totalmente gratuito (para o tamanho do dataset) e em cloud.

    ⚠ Caso prefira utilizar outro banco de dados de seu domínio também vale como problema resolvido.

### Tarefa 3: 
1. Criar objeto com operações de captura de dados, com atualização da tabela. O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela seja sempre atualizada com as últimas informações de reviews.

------

## Pré-requisitos


------

## Como rodar a aplicação

Tarefa 1 - Capturar dados de Loja de Aplicativo - Google Play
1. Acessar o Google Colab: https://colab.research.google.com/drive/1ak9TAlvzWBj5Hh39swM8iG-uF1dVaDe6?usp=sharing;
2. Acessar o diretótio do arquivo baixado: [google-play-scraper-alexa.ipynb](https://github.com/cicerooficial/desafio-case-python-sauter/blob/main/google_play_scraper_alexa.ipynb)

Tarefa 2 - Subir as tabelas para um BD
1. Abrir o [Console Cloud Google](https://console.cloud.google.com/);
2. Criar um novo projeto;
3. Acessar Cloud Storage e criar um Bucket:
    1. No Console do Cloud, acesse a página [**Navegador do Cloud Storage**](https://console.cloud.google.com/storage/browser?_ga=2.166776635.46602346.1640698504-1290315837.1637543424&_gac=1.88127977.1638926009.Cj0KCQiAqbyNBhC2ARIsALDwAsBz4QTdJRXbw46J7nxFQENlWuf6ztbFKXQj4eT0UeZnUu1ddWMQpp0aAhTXEALw_wcB);
    2. Clique em **Criar bucket(Create Bucket)**;
    3. Na página **Criar um bucket(Create a Bucket)**, insira as informações do seu bucket. Para ir à próxima etapa, clique em Continuar:
        - Em Nomear o bucket, insira um nome que atenda aos requisitos de nome de bucket;
        - Em Escolha onde armazenar os dados, selecione o Tipo de local e o Local onde os dados do bucket serão armazenados permanentemente;
        - Em Escolha uma classe de armazenamento padrão para os dados, selecione uma classe de armazenamento para o bucket. A classe de armazenamento padrão é atribuída por padrão a todos os objetos carregados no bucket;
        - Em Escolha como controlar o acesso a objetos, selecione se o bucket aplica a prevenção de acesso público e um modelo de Controle de acesso para os objetos do bucket;
        - Em Escolha como proteger os dados do objeto, configure **Ferramentas de proteção** se quiser e selecione um método de **Criptografia de dados**.
    4. Clique em **Criar(Create)**;
    5. CLique sobre o nome do Bucket criado e selecione a opção **FAZER UPLOAD DE ARQUIVOS(UPLOAD FILES)** e selecione os arquivos que deseja enviar para o CLOUD STORAGE.
4. No Menu, no grupo BigData, selecione em BigQuery;
5. Clique sobre os 3 pontos do ID do projeto e selecione a opção **Criar conjunto de dados(Create Dataset)**:
    1. Defina o código do conjunto de dados e o local dos dados. Dê preferência para mesmo região onde o bucket foi instanciado;
    2. Clique em **CRIAR CONJUNTO DE DADOS(CREATE DATASET)**.
6. Ao lado do nome do Conjunto de dados(Dataset) criado, clique sobre os 3 pontos e selecione a opção **Criar Tabela(Create Table)**:
    1. Em origem, defina como Google Cloud Storage;
    2. Selecione o caminho do bucket, até o arquivo da tabela que deseja importar os dados; 
    3. Em Destino, defina um nome para o conjunto de dados(dataset) a ser criada no BigQuery;
    4. Também defina um nome para a tabela a ser criada no BigQuery;
    5. Esquema(Schema) marque a caixa de seleção como detectar automaticamente;
    6. Em opção avançada, em Delimitador de campo(Field delimiter) selecione Personalizado e no campo abaixo digite ; como delimitar.
    7. Clique em **Criar tabela(Create table)** para concluir.

Tarefa 3 - Criar Pipeline de dados

------

## Linguagens, dependencias e libs utilizadas

|Lang/Lib/Framwork    |Version          |
|---------------------|---------        |
|Python               |3.6, 3.7 ou 3.8  |
|Google-Play-Scraper  |v1.0.2           |
|Pandas               |v1.3.5           |
|Pandas Profiling     |v3.1.0           |



------
## Referências

- [google-play-scraper 1.0.2](https://pypi.org/project/google-play-scraper/)
- [Pandas API reference](https://pandas.pydata.org/docs/reference/)
- [Package pandas_profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html)
- [Como criar buckets de armazenamento](https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-gsutil)
- 