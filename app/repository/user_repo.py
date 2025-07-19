from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI, DB_NAME
from app.models.user_model import User

client = AsyncIOMotorClient(MONGO_URI, tls=True)
db = client[DB_NAME]
collection = db["users"]

class UserRepository:
    async def create(self, user: User):
        await collection.insert_one(user.dict())
        return user

    async def get_all(self):
        users = await collection.find().to_list(100)
        return [self._convert_id(u) for u in users]

    async def get_by_username(self, username: str):
        user = await collection.find_one({"username": username})
        return self._convert_id(user) if user else None

    def _convert_id(self, user):
        user["id"] = str(user["_id"])
        del user["_id"]
        return user