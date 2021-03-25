from datetime import datetime

from pydantic import BaseModel, validator


class BooksSchema(BaseModel):
    title: str
    author: str
    pub_date: datetime
    isbn: str
    pages: int
    hyperlink: str
    language: str

    @validator("title", "author", "language", pre=True)
    def title_alphanumeric(cls, value):
        assert value.isalnum(), "must be alphanumeric"
        return value

    @validator("pub_date", pre=True)
    def parse_pub_date(cls, value):
        return datetime.strptime(value, "%d.%m.%Y").date()

    @validator("isbn", pre=True)
    def parse_isbn(cls, value):
        if len(value) != 17:
            raise ValueError("isbn number should contain 17 characters")
        return value

    @validator("pages")
    def check_pages(cls, value):
        if not isinstance(value, int):
            raise ValueError("pages should be an integer")
        elif value < 1:
            raise Exception("pages should have a least one page")
        return value
