import pytest

from app.model.product_models import ElectronicProduct, BookProduct


@pytest.fixture(scope='function')
def electronic_product():
    return ElectronicProduct(
        subcategory="TestProduct",
        brand="Dell",
        model="XPS 13",
        warranty_period=24,
        price=800,
        quantity=10
    )


@pytest.fixture(scope='function')
def another_electronic_product():
    return ElectronicProduct(
        subcategory="TestProduct",
        brand="Lenovo",
        model="XPS 13",
        warranty_period=24,
        price=1000,
        quantity=50
    )


@pytest.fixture(scope='function')
def book_product():
    return BookProduct(
        subcategory="Nonfiction",
        title="Reinventing Organizations",
        author="Frederic Lalu",
        publisher="Dell",
        ISBN="1223-456-zd4",
        price=120,
        quantity=7
    )
