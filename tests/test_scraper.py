from app.scraper import (
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
