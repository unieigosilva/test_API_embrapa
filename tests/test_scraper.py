from app.scraper import (
    scrape_production,
    scrape_processing,
    scrape_commercialization,
    scrape_import,
    scrape_export,
)

def test_scrape_production():
    year = 2021
    data = scrape_production(year)
    assert f"<table>" in data
    assert str(year) in data

def test_scrape_processing():
    category = "viniferas"
    data = scrape_processing(category)
    assert f"<table>" in data
    assert category in data.lower()

def test_scrape_commercialization():
    year = 2022
    data = scrape_commercialization(year)
    assert f"<table>" in data
    assert str(year) in data

def test_scrape_import():
    category = "vinhos_mesa"
    year = 2020
    data = scrape_import(category, year)
    assert f"<table>" in data
    assert category in data.lower()
    assert str(year) in data

def test_scrape_export():
    category = "espumantes"
    data = scrape_export(category)
    assert f"<table>" in data
    assert category in data.lower()