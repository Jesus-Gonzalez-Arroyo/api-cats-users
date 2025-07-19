from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserLogin

user_service = UserService()

async def create_user(user_data: UserCreate):
    return await user_service.create_user(user_data)

async def get_users():
    return await user_service.get_all_users()

async def login_user(user_data: UserLogin):
    return await user_service.authenticate_user(user_data)