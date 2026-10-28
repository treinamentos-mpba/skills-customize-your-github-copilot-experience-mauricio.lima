from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


class Book(BookInput):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    # Retorne um objeto JSON indicando que a API está funcionando.
    pass


@app.get("/books", response_model=list[Book])
def list_books():
    # Retorne todos os livros cadastrados.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    # Crie um livro com o próximo identificador e guarde-o em books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # Retorne o livro ou lance HTTPException com status 404.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # Atualize o livro ou lance HTTPException com status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Remova o livro ou lance HTTPException com status 404.
    # Retorne uma resposta vazia com status 204.
    pass