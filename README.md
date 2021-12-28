# Desafio: Capturar dados de Loja de Aplicativo - Google Play

## Tópicos:
- [Descrição do projeto](#descrição-do-projeto)
- [Objetivos](#objetivos)
- [Deploy da Aplicação](#deploy-da-aplicação)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar a aplicação](#como-rodar-a-aplicação)
- [Linguagens, dependencias e libs utilizadas](#linguagens,-dependencias-e-libs-utilizadas)
- [Tarefas em aberto](#tarefas-em-aberto)

------

## Descrição do projeto
O Desafio Python tem como objetivo reflitir alguns desafios que um Engenheiro de Dados possa enfrentar na Sauter.

⚠ É importante saber que há múltiplos formatos para a resolução do desafio e será necessário consultar documentações (algumas das quais colocaremos o link aqui).

------

## Objetivos

### ⬜ Tarefa 1: 
Sua primeira tarefa é utilizar a library google-play-scraper para capturar dados de apps.
O app selecionado é o [Alexa](https://play.google.com/store/apps/details?id=com.amazon.dee.app), da Amazon.
Utilizando as informações de avaliação do aplicativo, você deve chegar em um Data Frame de
review parecido com o demonstrado abaixo:

A partir desse Data Frame, seguem as atividades propostas na tarefa:

- Criar 3 arquivos .csv a partir do dataframe, com a seguinte classificação:
    1. aval_positiva.csv para score maior ou igual a 4; 
    2. aval_neutra.csv para score igual a 3;
    3. aval_negativa.csv para score inferior a 3.

- Criar um report simples para essas variáveis utilizando a library pandas profiling para
cada uma das separações (aval_neutra, aval_positiva, aval_negativa). </br>
⚠ É importante notar os principais pontos de cada análise para sua apresentação.</br>
Finalmente, salvar o resultado do profile em formato .html.

### ⬜ Tarefa 2: 
A partir dos dados criados, subir as tabelas para um banco de dados.

Aqui é completamente opcional qual banco de dados utilizar, mas considerar utilizar o [BigQuery](https://cloud.google.com/bigquery/docs/tables) da Google, pois é totalmente gratuito (para o tamanho do dataset) e em cloud.
Caso prefira utilizar outro banco de dados de seu domínio também vale como problema resolvido.

### ⬜ Tarefa 3: 
Criar objeto com operações de captura de dados, com atualização da tabela.
O objetivo aqui é criar um pipeline simplificado de dados para o banco, de forma que a tabela
seja sempre atualizada com as últimas informações de reviews.

------
## Deploy da Aplicação

------

## Pré-requisitos

------

## Como rodar a aplicação

------

## Linguagens, dependencias e libs utilizadas

------

## Tarefas em aberto