import requests
from bs4 import BeautifulSoup
import re
import html
import pandas
import json


BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"



def scrape_production(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
   
   #Convertende a tabela em um dataframe Json
    table = soup.find("table", class_="tb_base tb_dados")
    data = []

    if table:
        rows = table.find_all('tr')
        # Extrair cabeçalhos da tabela para usar como chaves nos dicionários
        headers = [th.text.strip() for th in rows[0].find_all('th')] if rows else []

        for row in rows[1:]:  # Ignorar a primeira linha que é o cabeçalho
            cells = row.find_all('td')
            if len(cells) == 2:  # Certificar que está pegando linhas com duas células
                entry = {headers[0]: cells[0].text.strip(), headers[1]: cells[1].text.strip()}
                data.append(entry)
    return data


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

    data = []
    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) == 2:
                entry = {
                    headers[0].replace("Cultivar ", "Cultivar"): cells[0].text.strip(),
                    headers[1].replace("Quantidade (Kg) ", "Quantidade (Kg)"): cells[1].text.strip()
                }
                data.append(entry)
    return data


def scrape_commercialization(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    data = []

    if table:
        rows = table.find_all('tr')
        # Extrair cabeçalhos da tabela para usar como chaves nos dicionários
        headers = [th.text.strip() for th in rows[0].find_all('th')] if rows else []

        for row in rows[1:]:  # Ignorar a primeira linha que é o cabeçalho
            cells = row.find_all('td')
            if len(cells) == 2:  # Certificar que está pegando linhas com duas células
                entry = {headers[0]: cells[0].text.strip(), headers[1]: cells[1].text.strip()}
                data.append(entry)
    return data


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

    data = []
    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) == 3:  # verifica se há três células conforme esperado
                entry = {
                    headers[0]: cells[0].text.strip(),
                    headers[1]: cells[1].text.strip() if cells[1].text.strip() != '-' else None,
                    headers[2]: cells[2].text.strip() if cells[2].text.strip() != '-' else None
                }
                data.append(entry)
    return data

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
    data = soup.find("table").prettify()
    table = soup.find("table", class_="tb_base tb_dados")

    data = []
    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            if len(cells) == 3:  # verifica se há três células conforme esperado
                entry = {
                    headers[0]: cells[0].text.strip(),
                    headers[1]: cells[1].text.strip() if cells[1].text.strip() != '-' else None,
                    headers[2]: cells[2].text.strip() if cells[2].text.strip() != '-' else None
                }
                data.append(entry)
    return data

"""
############################################################################################################
############################################################################################################
###################### Versão sem tratamento ###############################################################
############################################################################################################
############################################################################################################
"""
"""
def scrape_production(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find("table", class_="tb_base tb_dados").prettify()
    return data

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
    data = soup.find("table").prettify()
    return data

def scrape_commercialization(year):
    url = f"{BASE_URL}?ano={year}&opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find("table", class_="tb_base tb_dados").prettify()
    print(data)
    return data

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
    data = soup.find("table").prettify()
    print(data)
    return data

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
    data = soup.find("table").prettify()
    print(data)
    return data
"""
