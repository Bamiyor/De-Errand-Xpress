import pytest
from app import create_app, db
from app.models import Cart, User, Product

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

def test_get_all_carts(client):
    response = client.get('/api/v1/carts')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_cart(client):
    cart = Cart(user_id=1, product_id=1, quantity=1)
    cart.save()
    response = client.get(f'/api/v1/carts/{cart.id}')
    assert response.status_code == 200
    assert response.json['id'] == cart.id

def test_get_cart_not_found(client):
    response = client.get('/api/v1/carts/999')
    assert response.status_code == 404

def test_delete_cart(client):
    cart = Cart(user_id=1, product_id=1, quantity=1)
    cart.save()
    response = client.delete(f'/api/v1/carts/{cart.id}')
    assert response.status_code == 200
    response = client.get(f'/api/v1/carts/{cart.id}')
    assert response.status_code == 404

def test_delete_cart_not_found(client):
    response = client.delete('/api/v1/carts/999')
    assert response.status_code == 404

def test_post_cart(client):
    data = {'user_id': 1, 'product_id': 1, 'quantity': 1}
    response = client.post('/api/v1/carts', json=data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_post_cart_missing_fields(client):
    response = client.post('/api/v1/carts', json={})
    assert response.status_code == 400
    assert b'Missing user_id' in response.data or b'Missing product_id' in response.data or b'Missing quantity' in response.data

def test_post_cart_not_json(client):
    response = client.post('/api/v1/carts', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data

def test_put_cart(client):
    cart = Cart(user_id=1, product_id=1, quantity=1)
    cart.save()
    data = {'quantity': 5}
    response = client.put(f'/api/v1/carts/{cart.id}', json=data)
    assert response.status_code == 200
    assert response.json['quantity'] == 5

def test_put_cart_not_found(client):
    response = client.put('/api/v1/carts/999', json={'quantity': 5})
    assert response.status_code == 404

def test_put_cart_not_json(client):
    cart = Cart(user_id=1, product_id=1, quantity=1)
    cart.save()
    response = client.put(f'/api/v1/carts/{cart.id}', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data
