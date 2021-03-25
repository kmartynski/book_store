from sqlalchemy.orm import Session

from models import Book
from schemas import BooksSchema


def create_book(db: Session, book: BooksSchema, book_id: int):
    book_item = Book(**book.dict(), owner_id=book_id)
    db.add(book_item)
    db.commit()
    db.refresh(book_item)
    return book_item

