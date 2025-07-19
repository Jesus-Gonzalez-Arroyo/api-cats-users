from app.models.user_model import User
from app.repository.user_repo import UserRepository
from app.utils.username_generator import generate_username
from app.schemas.user_schema import UserCreate, UserLogin
from fastapi import HTTPException
from hashlib import sha256

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, data: UserCreate):
        username = generate_username(data.first_name, data.last_name)
        if await self.repo.get_by_username(username):
            raise HTTPException(status_code=400, detail="Ya existe este usuario")

        hashed_password = sha256(data.password.encode()).hexdigest()
        user_data = data.dict(exclude={"password"})
        user = User(**user_data, username=username, password=hashed_password)
        return await self.repo.create(user)

    async def get_all_users(self):
        return await self.repo.get_all()

    async def authenticate_user(self, data: UserLogin):
        user = await self.repo.get_by_username(data.username)
        if user and user["password"] == sha256(data.password.encode()).hexdigest():
            return user
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecta")
