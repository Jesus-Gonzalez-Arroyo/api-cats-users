from fastapi import FastAPI
from app.api.routes.cat_routes import router as CatRouter
from app.api.routes.user_routes import router as UserRouter

app = FastAPI(title="Cat & User API")

app.include_router(CatRouter, prefix="/breeds", tags=["Gatos"])
app.include_router(UserRouter, prefix="/user", tags=["Usuarios"])