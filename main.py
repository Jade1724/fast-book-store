from fastapi import FastAPI, HTTPException
import random 
import os
import json

app = FastAPI()

BOOKS_FILE = "books.json"
BOOK_DATABASE = [
    "The Greate Gatsby",
    "Atomic Habits",
    "Norwegian Wood"
]

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOK_DATABASE = json.load(f)
# /
@app.get("/")
async def home():
    return {"Message": "Welcome to my bookstore!"}

# /list-books
@app.get("/list-books")
async def list_books():
    return {"books": BOOK_DATABASE}

# /book-by-index/{index}
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < 0 or index > len(BOOK_DATABASE):
        raise HTTPException(404, f"Index {index} is out of range {len(BOOK_DATABASE)}.")
    else:
        return {"book": BOOK_DATABASE[index]}

# /get-random-book
@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_DATABASE)

# /add-book
@app.post("/add-book")
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE, f)
    return {"Message": f"Book {book} was added."}


# /get-book?id=...