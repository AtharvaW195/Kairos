from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_function() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_register_returns_jwt() -> None:
    response = client.post("/register", json={"email": "trader@example.com", "password": "securepass123"})
    assert response.status_code == 201
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_login_accepts_registered_user() -> None:
    client.post("/register", json={"email": "trader@example.com", "password": "securepass123"})
    response = client.post("/login", json={"email": "trader@example.com", "password": "securepass123"})
    assert response.status_code == 200
    assert response.json()["access_token"]


def test_login_rejects_invalid_credentials() -> None:
    response = client.post("/login", json={"email": "trader@example.com", "password": "securepass123"})
    assert response.status_code == 401
