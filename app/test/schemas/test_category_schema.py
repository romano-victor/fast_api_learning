import pytest
from app.schemas.category import Category

def test_category_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.model_dump() == {
        'name': 'Roupa',
        'slug': 'roupa'
    }


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='roupa com espaco'
        )

    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='roupá_com_acento'
        )

    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='RoupaComLetraMaiuscula'
        )


    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug=''
        )