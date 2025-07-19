from fastapi import APIRouter
from app.controllers.cat_controller import get_cats, get_cat_by_id, search_cats

router = APIRouter()

@router.get("/")
async def list_breeds():
    return await get_cats()

@router.get("/{breed_id}")
async def get_breed(breed_id: str):
    return await get_cat_by_id(breed_id)

@router.get("/search/")
async def search_breed(query: str):
    return await search_cats(query)