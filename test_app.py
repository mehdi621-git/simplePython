import pytest
from app import app

@pytest.fixture
def client():
    # Setup a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test that the home route returns a 200 status and correct message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json["status"] == "online"