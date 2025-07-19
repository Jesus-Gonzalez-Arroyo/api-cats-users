from app.services.cat_service import CatService

cat_service = CatService()

async def get_cats():
    return await cat_service.get_all_cats()

async def get_cat_by_id(id_cat: str):
    return await cat_service.get_cat(id_cat)

async def search_cats(query: str):
    return await cat_service.search_cat(query)