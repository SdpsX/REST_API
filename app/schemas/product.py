from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True