import requests
from bs4 import BeautifulSoup
import pandas as pd


def find_data_paper(code_paper, data_table, column_name):
    """
    Busca os dados de um papel na tabela e retorna um dicionário com esses dados.

    Args:
        code_paper (str): O código do papel a ser buscado.
        data_table (list): Lista de dicionários contendo os dados da tabela.
        column_name (str): Nome da coluna que contém os códigos dos papéis.

    Returns:
        dict: Um dicionário com os dados do papel, ou None se o papel não for encontrado.
    """
    for data in data_table:
        if data[column_name] == code_paper:
            return data
    return None


def main():
    # Pergunta ao usuário o número de papéis a serem consultados
    num_paper = int(input("Quantas Ações você deseja consultar? "))

    # Lista para armazenar os códigos dos papéis consultados
    papers_consulted = []

    # Solicita ao usuário que insira o código de cada papel individualmente
    for _ in range(num_paper):
        code_paper = input("Digite o Código das Ações: ").upper()
        papers_consulted.append(code_paper)

    # URL da página a ser consultada
    URL = "https://www.fundamentus.com.br/resultado.php"

    # Cabeçalho para simular um navegador
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Obtendo o conteúdo da página
    request = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(request.text, 'html.parser')

    # Encontrando a tabela de resultados
    table = soup.find('table', id='resultado')

    if table:
        data_table = []
        # Obtendo os nomes das colunas
        name_colums = [colum.text.strip()
                       for colum in table.find('tr').find_all(['th'])]
        print("Nomes das Colunas:", name_colums)  # Adicionado para depuração

        # Processando cada linha na tabela
        for line in table.find_all('tr')[1:]:
            cells = line.find_all(['td', 'th'])
            data_line = {}
            for i, cell in enumerate(cells):
                data_line[name_colums[i]] = cell.text.strip()
            data_table.append(data_line)

        # Lista para armazenar os dados dos papéis consultados
        data_papers = []

        # Buscando e armazenando os dados de cada papel consultado
        column_name = "Papel"  # Nome correto da coluna que contém os códigos dos papéis
        for paper in papers_consulted:
            paper_data = find_data_paper(paper, data_table, column_name)
            if paper_data:
                data_papers.append(paper_data)
            else:
                print(f"Dados não encontrados para a Ação {paper}")

        # Convertendo a lista de dicionários em um DataFrame do pandas
        if data_papers:
            df = pd.DataFrame(data_papers)
            # Exportando os dados para um arquivo Excel
            df.to_excel("data_papers.xlsx", index=False)
            print("Dados exportados para 'data_papers.xlsx' com sucesso.")
        else:
            print("Nenhum dado foi encontrado para os papéis consultados.")
    else:
        print("Tabela não encontrada.")


if __name__ == "__main__":
    main()
