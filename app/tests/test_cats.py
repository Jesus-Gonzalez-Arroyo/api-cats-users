import pytest
from httpx import AsyncClient
from app.main import app

""" Ejecutar con el servidor corriendo en docker """

@pytest.mark.asyncio
async def test_get_all_breeds():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        client._transport.app = app
        response = await client.get("/breeds/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_single_breed():
    cat_id = "beng"  # Puedes cambiar esto por una ID válida de raza de TheCatAPI
    async with AsyncClient(base_url="http://localhost:8000") as client:
        client._transport.app = app
        response = await client.get(f"/breeds/{cat_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == cat_id

@pytest.mark.asyncio
async def test_search_breeds():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        client._transport.app = app
        response = await client.get("/breeds/search/", params={"query": "bengal"})
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert any("bengal" in breed["name"].lower() for breed in data)
