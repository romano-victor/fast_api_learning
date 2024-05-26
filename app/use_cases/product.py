from app.db.models import Product as ProductModel
from app.db.models import Category as CategoryModel
from app.schemas.product import Product

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

class ProductUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_product(self, product: Product, category_slug: str):
        category = self.db_session.query(CategoryModel).filter(CategoryModel.slug == category_slug).first()

        if category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No category found with the given slug {category_slug}')

        product_db = ProductModel(
            name=product.name,
            slug=product.slug,
            price=product.price,
            stock=product.stock,
        )

        product_db.category_id = category.id
        
        self.db_session.add(product_db)
        self.db_session.commit()
    
    def update_product(self, id: int, product: Product):
        product_db = self.db_session.query(ProductModel).filter(ProductModel.id == id).first()

        if product_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No product found with the given id {id}')

        product_db.name = product.name
        product_db.slug = product.slug
        product_db.price = product.price
        product_db.stock = product.stock

        self.db_session.add(product_db)
        self.db_session.commit()
    

    def delete_product(self, id: int):
        product_db = self.db_session.query(ProductModel).filter(ProductModel.id == id).first()

        if product_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No product found with the given id {id}')

        self.db_session.delete(product_db)
        self.db_session.commit()