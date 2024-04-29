import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel

@pytest.fixture
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture
def categories_on_db(db_session):
    categories = [
        CategoryModel(name='Roupa', slug='roupa'),
        CategoryModel(name='Eletrônicos', slug='eletronicos'),
        CategoryModel(name='Livros', slug='livros'),
        CategoryModel(name='Alimentos', slug='alimentos'),
    ]

    for category in categories:
        db_session.add(category)
    
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    
    yield categories

    for category in categories:
        db_session.delete(category)

    db_session.commit()