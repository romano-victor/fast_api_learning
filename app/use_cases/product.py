from app.db.models import Product as ProductModel
from app.schemas.product import Product
from sqlalchemy.orm import Session

class ProductUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_product(self, product: Product, category_slug: str):
        product_db = ProductModel(
            name=product.name,
            slug=product.slug,
            price=product.price,
            stock=product.stock,
        )

        self.db_session.add(product_db)
        self.db_session.commit()