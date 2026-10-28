import books_api
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    books_api.books.clear()
    books_api.next_book_id = 1

    with TestClient(books_api.app) as test_client:
        yield test_client

    books_api.books.clear()
    books_api.next_book_id = 1


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_books_starts_empty(client):
    response = client.get("/books")

    assert response.status_code == 200
    assert response.json() == []
