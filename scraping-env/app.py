from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
import requests

# ANO DA TEMPORADA QUE SERÁ ANALISADA
year = 2023

# URL DA PÁGINA PARA COLETA DOS DADOS
url_nba = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# CRIANDO A VARIÁVEL PAGE E UTILIZANDO O MÉTODO REQUESTS PARA COLETA DOS DADOS
page = requests.get(url_nba)

# VISUALIZANDO A PERMISSÃO DA URL PARA COLETA DE DADOS
print(page)

# CRIANDO VARIÁVEIS PARA ATRIBUIREM A URL PARA COLETA E EXTRAÇÃO DOS DADOS
html_nba = urlopen(url_nba)
soup_nba = BeautifulSoup(html_nba, features="html.parser")


# INFORMANDO AS TAGS ONDE ESTÃO OS CÓDIGOS QUE SERÃO COLETADOS (as tags linhas estão dentro da tag td)
rows = soup_nba.findAll('tr')[1:]
players_stats_2023 = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]


# VISUALIZANDO O CABEÇALHO DAS COLUNAS
headers_2023 = [th.getText() for th in soup_nba.findAll('tr', limit=2)[0].findAll('th')]
print(headers_2023)