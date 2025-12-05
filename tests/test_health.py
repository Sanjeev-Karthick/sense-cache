from fastapi.testclient import TestClient
from sensecache.server import app

client = TestClient(app)

def test_health_check():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
