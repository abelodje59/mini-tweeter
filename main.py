from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model
from models.twitter import User
from views.twitter import user_views
from core.config import settings
from tortoise.contrib.fastapi import register_tortoise


app=FastAPI()
register_tortoise(
    app,
    db_url=settings.SQLITE_URL,
    modules={"models": [settings.TORTOISE_MODELS]},
    generate_schemas=True,
    add_exception_handlers=True,
)
app.include_router(
    user_views,
    tags=["Users"])