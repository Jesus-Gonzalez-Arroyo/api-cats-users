import httpx
from app.core.config import API_KEY

class CatService:
    BASE_URL = "https://api.thecatapi.com/v1"
    headers = {"x-api-key": API_KEY}

    async def get_all_cats(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}/breeds", headers=self.headers)
            return response.json()

    async def get_cat(self, cat_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}/breeds/{cat_id}", headers=self.headers)
            return response.json()

    async def search_cat(self, query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}/breeds/search?name={query}", headers=self.headers)
            return response.json()