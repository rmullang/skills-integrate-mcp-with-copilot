import os
from pathlib import Path

# Ensure test DB is isolated
os.environ["DATABASE_URL"] = "sqlite:///./test_data.db"

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_create_and_list_user():
    # Create a user
    res = client.post("/users", json={"email": "test@example.com", "full_name": "Test User", "password": "secret"})
    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "test@example.com"

    # List users
    res2 = client.get("/users")
    assert res2.status_code == 200
    users = res2.json()
    assert any(u["email"] == "test@example.com" for u in users)

    # Cleanup test DB file
    db_path = Path("test_data.db")
    if db_path.exists():
        db_path.unlink()
