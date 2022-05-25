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

def test_add_user():
    response = client.post(
        "/users",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "is_active": False
        }
    )
    assert response.status_code == 201
    assert response.json()["data"]["first_name"] == "John"
    assert response.json()["data"]["last_name"] == "Doe"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 1

def test_update_user():
    response = client.put(
        "/users/2",
        json={
            "first_name": "Edited",
            "last_name": "Edited",
            "email": "edited@edited.com",
            "is_active": True
        }
    )
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "Edited"
    assert response.json()["data"]["last_name"] == "Edited"
