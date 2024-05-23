# Import Bibliotecas
import os
import requests
from bs4 import BeautifulSoup

# Constante URL
URL = "https://br.investing.com/currencies/usd-brl"

# Constante USER-AGENT
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Requisição
request = requests.get(URL, headers=HEADERS)

# Trazendo o HTML organizado e chamando isso de soup
soup = BeautifulSoup(request.text, 'html.parser')

# Procurando no site, uma "DIV" Com a Classe referente a cotação
cota_hoje = soup.find(
    "div", class_="text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]")

# Extraindo o texto e também usando .strip() pra tirar os espaços
texto_cota_hoje = cota_hoje.text.strip()

# Transformando em float e colocando "replace" ". no lugar de ,"
cota_hoje_float = float(texto_cota_hoje.replace(',', '.'))
# Mensagem junto com o print
print(f"Cotação do Dolar Hoje! {cota_hoje_float}")

# Mantem o console aberto, de maneira "elegante"
# Pede para pressionar qualquer tecla, assim ele fecha
# Porém precisa importar a Biblioteca "os" com "import os"
os.system('pause')
