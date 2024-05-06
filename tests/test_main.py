from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_production_data():
    response = client.get("/production/?year=2021")
    assert response.status_code == 200  # Verifica se o status da resposta é 200
    assert response.json()['year'] == 2021  # Verifica se o ano na resposta é correto
