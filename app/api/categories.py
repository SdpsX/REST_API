from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.db import get_db

router = APIRouter()

@router.get("/categories/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories