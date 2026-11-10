import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

DATABASE_PATH = Path(__file__).with_name("books.db")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with get_connection() as connection:
        # TODO: Create the books table if it does not exist.
        pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(title="Book Catalog API", lifespan=lifespan)


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Read all books from SQLite and return them as dictionaries.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Find the requested book or raise HTTPException with status 404.
    pass


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_input: BookInput):
    # TODO: Insert the book and return it with its generated database ID.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: Update the book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTPException with status 404.
    return Response(status_code=204)