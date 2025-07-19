from fastapi import APIRouter
from app.controllers.user_controller import create_user, get_users, login_user
from app.schemas.user_schema import UserCreate, UserLogin

router = APIRouter()

@router.get("/")
async def list_users():
    return await get_users()

@router.post("/")
async def register_user(user: UserCreate):
    return await create_user(user)

@router.post("/login")
async def login(user: UserLogin):
    return await login_user(user)