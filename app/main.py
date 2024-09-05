from fastapi import FastAPI
from app.api import products, categories
from app.db import Base, engine

app = FastAPI()

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app.include_router(products.router)
app.include_router(categories.router)