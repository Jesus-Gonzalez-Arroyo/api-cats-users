from fastapi.testclient import TestClient
from app.main import app
import pytest
from httpx import AsyncClient

client = TestClient(app)

""" Cambiar nombre y apellido si desea que responda con status 200 """

def test_create_user():
    response = client.post("/user", json={
        "first_name": "Test5",
        "last_name": "User5",
        "password": "123456"
    })
    assert response.status_code == 200 or response.status_code == 400


""" Ejecutar con el servidor corriendo en docker """

@pytest.mark.asyncio
async def test_login_user():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        client._transport.app = app

        response = await client.post("/user/login", json={
            "username": "test.user",
            "password": "123456"
        })
        assert response.status_code == 200