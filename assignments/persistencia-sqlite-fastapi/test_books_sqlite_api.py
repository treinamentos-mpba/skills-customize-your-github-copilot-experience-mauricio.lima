import pytest
from fastapi.testclient import TestClient

import books_sqlite_api


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Cada teste usa um banco temporário e limpo
    monkeypatch.setenv("BOOKS_DB_PATH", str(tmp_path / "test_books.db"))
    books_sqlite_api.init_db()
    return TestClient(books_sqlite_api.app)


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_book(client):
    payload = {"title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}

    created = client.post("/books", json=payload)

    assert created.status_code == 201
    assert created.json() == {"id": 1, **payload}
    assert client.get("/books/1").json() == created.json()


# TODO: teste de listagem, atualização e remoção
# TODO: testes de 404 para GET, PUT e DELETE com id inexistente
# TODO: teste de persistência abrindo uma nova conexão com books_sqlite_api.get_connection()
