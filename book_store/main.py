from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database import SessionLocal, engine
from models import Base, Book
from schemas import BooksSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/books", response_model=List[BooksSchema])
async def get_all_books(db: Session = Depends(get_db)):
    records = db.query(Book).all()
    return records


@app.post("/books")
async def post_book():
    pass
