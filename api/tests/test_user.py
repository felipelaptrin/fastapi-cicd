from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_existing_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "Nannette"

def test_get_non_existing_user():
    response = client.get("/users/-1")
    assert response.status_code == 404
