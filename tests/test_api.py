import pytest
from server.api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_all_berry_stats(client):
    response = client.get("/allBerryStats")
    assert response.status_code == 200
