from fastapi.testclient import TestClient
import os

from main import app

os.environ["TEST"] = "True"
os.environ["BOOKS"] = "[]"
os.environ["USERS"] = "[]"

client = TestClient(app)

todos = {}

def test_post_create_libro():
    response = client.post('/libro/create/', json={"id": 6,"title": "Libro 6","autor": "Autor del libro Test","disponible": True},headers={
        'accept':'application/json',
        'Content-Type':'application/json'
    })
    assert response.status_code == 200

def test_post_create_usuario():
    response = client.post('/usuario/create/', json={"id": 6,"nombre": "Usuario test","libros_prestados": "[]"},headers={
        'accept':'application/json',
        'Content-Type':'application/json'
    })

    assert response.status_code == 200

def test_post_prestar_book():
    response = client.post('/usuario/prestar_libro/usario_id/1?usuario_id=1',headers={
        'accept':'application/json',
        'Content-Type':'application/json'
    })
    assert response.status_code == 200


