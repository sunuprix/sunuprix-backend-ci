from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_retourne_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_documentation_openapi_disponible():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/health" in response.json()["paths"]
