import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel

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


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name='teste_product', slug='teste_product')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
        category_id = category.id
        )

    db_session.add(product)
    db_session.commit()

    db_session.refresh(product)

    yield product

    db_session.delete(category)
    db_session.delete(product)
    db_session.commit()