import pytest
from fastapi import HTTPException
from app.db.models import Product as ProductModel
from app.schemas.product import Product
from app.use_cases.product import ProductUseCases

def test_add_product_uc(db_session, categories_on_db):
    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
    )

    product_uc = ProductUseCases(db_session)
    product_uc.add_product(product=product, category_slug=categories_on_db[0].slug)

    product_db = db_session.query(ProductModel).first()

    assert product_db is not None
    assert product_db.name == product.name
    assert product_db.slug == product.slug
    assert product_db.price == product.price
    assert product_db.stock == product.stock
    assert product_db.category.name == categories_on_db[0].name

    db_session.delete(product_db)
    db_session.commit()

def test_invalid_category_slug_add_product_uc(db_session):
    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
    )

    product_uc = ProductUseCases(db_session)

    with pytest.raises(HTTPException):
        product_uc.add_product(product=product, category_slug='invalid-slug')

def test_update_product(db_session, product_on_db):
    uc = ProductUseCases(db_session=db_session)

    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
    )

    uc.update_product(
        id=product_on_db.id,
        product=product
    )

    product_db = db_session.query(ProductModel).filter(ProductModel.id == product_on_db.id).first()

    assert product_db is not None
    assert product_db.name == product.name
    assert product_db.slug == product.slug
    assert product_db.price == product.price
    assert product_db.stock == product.stock


def test_update_product_invalid_id(db_session):
    uc = ProductUseCases(db_session=db_session)

    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10
    )

    with pytest.raises(HTTPException):
        uc.update_product(
            id=0,
            product=product
        )

def test_delete_product(db_session, product_on_db):
    uc = ProductUseCases(db_session=db_session)

    uc.delete_product(id=product_on_db.id)

    product_db = db_session.query(ProductModel).filter(ProductModel.id == product_on_db.id).first()

    assert product_db is None


def test_delete_product_invalid_id(db_session):
    uc = ProductUseCases(db_session=db_session)

    with pytest.raises(HTTPException):
        uc.delete_product(id=1)