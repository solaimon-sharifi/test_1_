"""Integration tests for FastAPI endpoints in calculator.main."""
from fastapi.testclient import TestClient

from calculator.main import app


client = TestClient(app)


def test_add_endpoint():
    resp = client.post("/api/add", json={"left": 1, "right": 2})
    assert resp.status_code == 200
    assert resp.json()["result"] == 3


def test_subtract_endpoint():
    resp = client.post("/api/subtract", json={"left": 5, "right": 3})
    assert resp.status_code == 200
    assert resp.json()["result"] == 2


def test_multiply_endpoint():
    resp = client.post("/api/multiply", json={"left": 2, "right": 4})
    assert resp.status_code == 200
    assert resp.json()["result"] == 8


def test_divide_endpoint():
    resp = client.post("/api/divide", json={"left": 10, "right": 2})
    assert resp.status_code == 200
    assert resp.json()["result"] == 5


def test_divide_by_zero_endpoint():
    resp = client.post("/api/divide", json={"left": 1, "right": 0})
    assert resp.status_code == 400
    assert "Cannot divide by zero" in resp.json().get("detail", "")
