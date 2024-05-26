from sqlalchemy.orm import Session
from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput

from fastapi import HTTPException, status

class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_category(self, category: Category):
        category_model = CategoryModel(
            name=category.name,
            slug=category.slug
        )

        self.db_session.add(category_model)
        self.db_session.commit()

    def list_categories(self):
        categories_output = self.db_session.query(CategoryModel).all()
        categories_output = [
            self.serialize_category(category) for category in categories_output
        ]

        return categories_output


    def delete_category(self, id: int):
        category = self.db_session.query(CategoryModel).filter_by(id=id).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
        
        self.db_session.delete(category)
        self.db_session.commit()
    
    
    def serialize_category(self, category: CategoryModel):
        return CategoryOutput(**category.__dict__)