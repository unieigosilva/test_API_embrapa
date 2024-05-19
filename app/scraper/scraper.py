import requests
from bs4 import BeautifulSoup

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

def extract_data_from_table(table):
    # Extrai os dados de uma tabela HTML e retorna uma lista de dicionários
    data = []
    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if cells:
                entry = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
                data.append(entry)
    return data

def scrape_production(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)

def scrape_processing(category, year=None):
    category_map = {
        "viniferas": "subopt_01",
        "americanas_hibridas": "subopt_02",
        "uvas_mesa": "subopt_03",
        "sem_classificacao": "subopt_04",
    }
    params = {"opcao": "opt_03", "subopcao": category_map[category]}
    if year:
        params["ano"] = year
    url = f"{BASE_URL}?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)

def scrape_commercialization(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)

def scrape_import(category, year=None):
    category_map = {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "uvas_passas": "subopt_04",
        "suco_uva": "subopt_05",
    }
    params = {"opcao": "opt_05", "subopcao": category_map[category]}
    if year:
        params["ano"] = year
    url = f"{BASE_URL}?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)

def scrape_export(category, year=None):
    category_map = {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "suco_uva": "subopt_04",
    }
    params = {"opcao": "opt_06", "subopcao": category_map[category]}
    if year:
        params["ano"] = year
    url = f"{BASE_URL}?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)
