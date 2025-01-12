from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI();


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


BOOKS = []
@app.get("/")
def get_books():
    return BOOKS


@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.put("/update/{book_id}")
def update_book(book: Book, book_id: UUID):

    for i in range(0, len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS[i] = book
            return BOOKS[i]
    raise HTTPException(
        status_code=401,
        detail=f"ID: {book_id}: Does not exist"
    )

@app.delete("/delete/{book_id}")
def delete_book(book_id: UUID):

    for i in range(0, len(BOOKS)):
        if BOOKS[i].id == book_id:
            del BOOKS[i]
            return f"ID: {book_id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )