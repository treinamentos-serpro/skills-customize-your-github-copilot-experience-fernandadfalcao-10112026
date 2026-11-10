from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    2: Book(id=2, title="Kindred", author="Octavia E. Butler"),
}