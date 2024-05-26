import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel


class Product(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int

    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Slug must have only letters, hyphens and underscores')
        
        return value
    
    @field_validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than zero')
        
        return value
    
    @field_validator('stock')
    def validate_stock(cls, value):
        if value < 0:
            raise ValueError('Stock must be greater than or equal to zero')
        
        return value


class ProductInput(CustomBaseModel):
    category_slug: str
    product: Product