from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home(client: TestClient) -> None:

    response = client.get("/api/users")
    assert response.status_code == 200

