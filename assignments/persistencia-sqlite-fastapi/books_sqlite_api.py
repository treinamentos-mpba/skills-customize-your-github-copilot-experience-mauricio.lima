import os
import sqlite3

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Books API (SQLite)")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


class Book(BookInput):
    id: int


def get_connection() -> sqlite3.Connection:
    # TODO: conectar em os.environ.get("BOOKS_DB_PATH", "books.db")
    # e configurar row_factory = sqlite3.Row
    raise NotImplementedError


def init_db() -> None:
    # TODO: criar a tabela books (id, title, author, year) se não existir
    raise NotImplementedError


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: SELECT de todos os livros
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    # TODO: INSERT parametrizado e retornar o livro com o id gerado (lastrowid)
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: SELECT por id; 404 se não existir
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: UPDATE por id; 404 se nenhuma linha for alterada (rowcount)
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: DELETE por id; 404 se nenhuma linha for removida
    raise NotImplementedError
