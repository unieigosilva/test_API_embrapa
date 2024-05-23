import requests
from bs4 import BeautifulSoup
from app.config import scraper  # Importar o novo dicionário do arquivo config.py


BASE_URL = scraper['base_url']

def extract_data_from_table(table):
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
    params = {"opcao": "opt_03", "subopcao": scraper['processing'][category]}
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
    params = {"opcao": "opt_05", "subopcao": scraper['import'][category]}
    if year:
        params["ano"] = year
    url = f"{BASE_URL}?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)

def scrape_export(category, year=None):
    params = {"opcao": "opt_06", "subopcao": scraper['export'][category]}
    if year:
        params["ano"] = year
    url = f"{BASE_URL}?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return extract_data_from_table(table)
