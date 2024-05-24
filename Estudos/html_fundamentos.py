# Bibliotecas
import os
import requests
from bs4 import BeautifulSoup

# Constantes
URL = "https://www.fundamentus.com.br/resultado.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Requisição
request = requests.get(URL, headers=HEADERS)

# Site organizado
soup = BeautifulSoup(request.text, 'html.parser')

# Tabela de resultados
table = soup.find_all('table', id='resultado')

# Dados da tabela - Lista vazia
if table:
    data_table = []

# Nome da coluna = Dentro dessa lista vazia [] vc vai pegar o texto da coluna, sem espaços [colum.text.strip()]
# Para cada coluna do site organizado [for colum in soup]
# Procure "Table Rows" Linhas da tabela [soup.find('tr')]
# E em todas as linhas procure tudo que for cabeçalho ('tr').find_all(['th'])

    name_colums = [colum.text.strip()
                   for colum in soup.find('tr').find_all(['th'])]
    print(name_colums)
