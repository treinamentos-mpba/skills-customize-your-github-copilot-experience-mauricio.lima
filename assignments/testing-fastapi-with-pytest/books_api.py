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
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    return list(books.values())


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    global next_book_id

    book = Book(id=next_book_id, **book_input.model_dump())
    books[book.id] = book
    next_book_id += 1
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    book = Book(id=book_id, **book_input.model_dump())
    books[book_id] = book
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    del books[book_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
