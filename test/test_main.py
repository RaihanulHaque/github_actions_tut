from fastapi.testclient import TestClient
from ..main import app, add_numbers

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200  # Checks if API responds OK
    assert response.json() == {"message": "Hello, World!"}  # Checks the message

def test_add():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_multiply():
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}

def test_add_numbers_function():
    assert add_numbers(1, 2) == 3  # Tests the simple function