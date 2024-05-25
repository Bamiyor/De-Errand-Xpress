#!/usr/bin/python3

import pytest
from sqlalchemy import create_engine, inspect
from de_errand_xpress.errand_models.errand_models import Base, Errand, User, Product, Cart  # Adjust the import paths if necessary

@pytest.fixture(scope='module')
def test_engine():
    # Use an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope='module')
def connection(test_engine):
    connection = test_engine.connect()
    yield connection
    connection.close()

def test_tables_created(connection):
    inspector = inspect(connection)
    tables = inspector.get_table_names()

    assert 'errand' in tables
    assert 'user' in tables
    assert 'product' in tables
    assert 'cart' in tables


