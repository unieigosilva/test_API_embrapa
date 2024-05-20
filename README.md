```markdown
# TEST_API_EMBRAPA


> Linha adicional de texto informativo sobre o que o projeto faz. Sua introdução deve ter cerca de 2 ou 3 linhas. Não exagere, as pessoas não vão ler.

Descrição breve do projeto, explicando o que ele faz e qual problema resolve.


## Sobre o Projeto
Este projeto consiste em uma API pública desenvolvida em Python com FastAPI para consultar dados do site da Embrapa nas categorias de Produção, Processamento, Comercialização, Importação, e Exportação. Os objetivos incluem:
1. Criar uma Rest API em Python que faça a consulta no site da Embrapa.
2. Documentar a API.
3. Implementar um método de autenticação (JWT).
4. Criar um plano para fazer o deploy da API.
5. Fazer um MVP realizando o deploy com um link compartilhável e um repositório no GitHub.


### Estrutura do Projeto:
    .
    TEST_API_EMBRAPA/
    ├── app/
    │   ├── __init__.py
    │   ├── data_processing/
    │   │   ├── __init__.py
    │   │   ├── comercializacao_processing.py
    │   │   ├── exportacao_processing.py
    │   │   ├── importacao_processing.py
    │   │   ├── processamento_processing.py
    │   │   ├── producao_processing.py
    │   │   └── database_update.py
    │   │
    │   ├── sql_app/
    │   │   ├── __init__.py
    │   │   ├── database_manager.py
    │   │   ├── database.py
    │   │   ├── dependencies.py
    │   │   ├── embrapa.db
    │   │   └── models.py 
    │   │
    │   ├── scraper/
    │   │   ├── __init__.py
    │   │   ├── models.py.py
    │   │   └─── scraper.py
    │   │   
    │   │
    │   ├──__init__.py 
    │   ├── main.py
    │   └── config.py
    │    
    ├── Docker/
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   ├── initialize.py    
    │   ├── requirements.txt       
    │   └── .dockerignore
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_main.py
    │   └── test_scraper.py
    │
    ├──VENV/
    │
    ├── README.md
    └── .gitignore


## Construído Com
- Python
- FastAPI
- SQLAlchemy
- Docker
- JWT para autenticação

## Começando

## 💻 Pré-requisitos
- Docker
- Docker Compose

### Roteiro

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Tarefa 1
- [x] Tarefa 2
- [x] Tarefa 3
- [ ] Tarefa 4
- [ ] Tarefa 5


## 🚀 Instalando <nome_do_projeto>
Para instalar o <nome_do_projeto>, siga estas etapas:

Linux e macOS:

```
<comando_de_instalação>
```
Windows:
```
<comando_de_instalação>
```

## ☕ Usando <nome_do_projeto>
Para usar <nome_do_projeto>, siga estas etapas:

```
<exemplo_de_uso>
```
Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Fornece uma referência de opções para pontos de bônus! Aqui quero adicionar um gif com execução pratica.

### Testes
- Os testes são realizados para garantir que a API e os scrapers funcionem corretamente. Eles utilizam o FastAPI TestClient e Pytest para realizar testes de integração.

## Objetivo dos Testes de Integração
-O principal objetivo é verificar se os diferentes componentes da sua API (rotas, controladores, modelos, banco de dados, etc.)     funcionam corretamente em conjunto, simulando requisições HTTP reais.
## Estrutura dos Testes
-Os arquivos de testes estão localizados no diretório tests/.
    .
    tests/
    ├── __init__.py
    ├── test_main.py
    └── test_scraper.py
## Testes com FastAPI: TestClient e Pytest
```
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_production_data():
    response = client.get("/production/?year=2021")
    assert response.status_code == 200  # Verifica se o status da resposta é 200
    assert response.json()['year'] == 2021  # Verifica se o ano na resposta é correto
```

## Exemplo de Teste de rota Scraping em test_scraper.py:
```
from app.scraper.scraper import (
    scrape_production,
    scrape_processing,
    scrape_commercialization,
    scrape_import,
    scrape_export,
)

def test_scrape_production():
    # Supondo que você espera que a função retorne uma lista de dicionários para o ano 2021
    result = scrape_production(2021)
    assert type(result) == list  # Verifica se o resultado é uma lista
    assert len(result) > 0  # Verifica se a lista não está vazia
    assert 'Produto' in result[0]  # Verifica se a chave esperada está no dicionário
```
## Exemplo de Teste de Integração para Banco de Dados em test_db.py:
```
from app.sql_app.database import get_db
from app.sql_app.models import Production
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_database_connection():
    # Código de teste para verificar a conexão com o banco de dados
```

## Executando os Testes
Para rodar os testes, use o seguinte comando

## 📫 Contribuindo para <nome_do_projeto>
Este projeto foi desenvolvido individualmente. As bibliotecas e fontes de dados utilizadas incluem:

- FastAPI
- SQLAlchemy
- BeautifulSoup
- Requests

### 📝 Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE.md para mais detalhes

### Contato

### Agradecimentos
Prof. Nome do Professor 1
Prof. Nome do Professor 2

## Plano de Deploy
[Espaço reservado para o plano de deploy]

