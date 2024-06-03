import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

def test_get_all_users(client):
    response = client.get('/api/v1/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_user(client):
    user = User(email='test@example.com', password='password')
    user.save()
    response = client.get(f'/api/v1/users/{user.id}')
    assert response.status_code == 200
    assert response.json['id'] == user.id

def test_get_user_not_found(client):
    response = client.get('/api/v1/users/999')
    assert response.status_code == 404

def test_delete_user(client):
    user = User(email='test@example.com', password='password')
    user.save()
    response = client.delete(f'/api/v1/users/{user.id}')
    assert response.status_code == 200
    response = client.get(f'/api/v1/users/{user.id}')
    assert response.status_code == 404

def test_delete_user_not_found(client):
    response = client.delete('/api/v1/users/999')
    assert response.status_code == 404

def test_post_user(client):
    data = {'email': 'new@example.com', 'password': 'newpassword'}
    response = client.post('/api/v1/users', json=data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_post_user_missing_fields(client):
    response = client.post('/api/v1/users', json={})
    assert response.status_code == 400
    assert b'Missing email' in response.data or b'Missing password' in response.data

def test_post_user_not_json(client):
    response = client.post('/api/v1/users', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data

def test_put_user(client):
    user = User(email='test@example.com', password='password')
    user.save()
    data = {'password': 'newpassword'}
    response = client.put(f'/api/v1/users/{user.id}', json=data)
    assert response.status_code == 200
    assert response.json['password'] == 'newpassword'

def test_put_user_not_found(client):
    response = client.put('/api/v1/users/999', json={'password': 'newpassword'})
    assert response.status_code == 404

def test_put_user_not_json(client):
    user = User(email='test@example.com', password='password')
    user.save()
    response = client.put(f'/api/v1/users/{user.id}', data="not a json")
    assert response.status_code == 400
    assert b'Not a JSON' in response.data
