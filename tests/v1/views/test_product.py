import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

def test_get_all_products(client):
    response = client.get('/api/v1/products')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_product(client):
    product = Product(name='Test Product', price=10.0)
    product.save()
    response = client.get(f'/api/v1/products/{product.id}')
    assert response.status_code == 200
    assert response.json['id'] == product.id

def test_get_product_not_found(client):
    response = client.get('/api/v1/products/999')
    assert response.status_code == 404

def test_delete_product(client):
    product = Product(name='Test Product', price=10.0)
    product.save()
    response = client.delete(f'/api/v1/products/{product.id}')
    assert response.status_code == 200
    response = client.get(f'/api/v1/products/{product.id}')
    assert response.status_code == 404

def test_delete_product_not_found(client):
    response = client.delete('/api/v1/products/999')
    assert response.status_code == 404

def test_post_product(client):
    data = {'name': 'New Product', 'price': 20.0}
    response = client.post('/api/v1/products', json=data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_post_product_missing_fields(client):
    response = client.post('/api/v1/products', json={})
    assert response.status_code == 400
    assert b'Missing name' in response.data or b'Missing price' in response.data

def test_post_product_not_json(client):
    response = client.post('/api/v1/products', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data

def test_put_product(client):
    product = Product(name='Test Product', price=10.0)
    product.save()
    data = {'price': 15.0}
    response = client.put(f'/api/v1/products/{product.id}', json=data)
    assert response.status_code == 200
    assert response.json['price'] == 15.0

def test_put_product_not_found(client):
    response = client.put('/api/v1/products/999', json={'price': 15.0})
    assert response.status_code == 404

def test_put_product_not_json(client):
    product = Product(name='Test Product', price=10.0)
    product.save()
    response = client.put(f'/api/v1/products/{product.id}', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data

