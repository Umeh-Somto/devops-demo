import pytest

from app.main import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index_returns_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.get_json()


def test_unknown_route_returns_404(client):
    assert client.get("/nope").status_code == 404