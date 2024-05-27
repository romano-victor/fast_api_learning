import pytest
from app.schemas.product import Product, ProductInput, ProductOutput
from app.schemas.category import Category

def test_product_schema():
    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
    )

    assert product.model_dump() == {
        'name': 'Camiseta',
        'slug': 'camiseta',
        'price': 50.0,
        'stock': 10,
    }

def test_product_schema_invalid_slug():
    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='Camiséta',
            price=50.0,
            stock=10,
        )

    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='Camiseta com espacos',
            price=50.0,
            stock=10,
        )
    
    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='camiseta-com-caracteres-especiais-@',
            price=50.0,
            stock=10,
        )


def test_product_schema_invalid_price():
    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='camiseta',
            price=0.0,
            stock=10,
        )

    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='camiseta',
            price=-50.0,
            stock=10,
        )


def test_product_schema_invalid_stock():
    with pytest.raises(ValueError) as excinfo:
        product = Product(
            name='Camiseta',
            slug='camiseta',
            price=50.0,
            stock=-10,
        )

def test_product_input_schema():
    product = Product(
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
    )
    product_input = ProductInput(
        category_slug='roupa',
        product=product
    )

    assert product_input.model_dump() == {
        'category_slug': 'roupa',
        'product': {
            'name': 'Camiseta',
            'slug': 'camiseta',
            'price': 50.0,
            'stock': 10,
        }

    }


def test_product_output_schema():
    category = Category(
        id=1,
        name='teste_product',
        slug='teste_product'
    )
    
    product_output = ProductOutput(
        id=1, 
        name='Camiseta',
        slug='camiseta',
        price=50.0,
        stock=10,
        category=category
    )

    assert product_output.model_dump() == {
        'id': 1,
        'name': 'Camiseta',
        'slug': 'camiseta',
        'price': 50.0,
        'stock': 10,
        'category': {
            'id': 1,
            'name': 'teste_product',
            'slug': 'teste_product'}
    }