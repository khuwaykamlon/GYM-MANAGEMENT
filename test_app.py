import pytest
from app import app, db, Member

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_homepage(client):
    """Test if the homepage loads correctly"""
    response = client.get('/')
    assert response.status_code == 200

def test_register_member(client):
    """Test member registration"""
    response = client.post('/register', data={'username': 'testuser', 'password': 'password123', 'rfid_tag': '123456'})
    assert response.status_code == 200
    assert b"Registration successful" in response.data
