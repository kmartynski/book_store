from sqlalchemy import String, Integer, Column, DateTime

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, nullable=False)
    author = Column(String, unique=False, nullable=False)
    pub_date = Column(DateTime)
    isbn = Column(String, unique=True, nullable=False)
    pages = Column(Integer, unique=False, nullable=False)
    hyperlink = Column(String, unique=False, nullable=False)
    language = Column(String, unique=False, nullable=False)
