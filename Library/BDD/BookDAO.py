from sqlalchemy import Column, Integer, String
from .Context import Base
from DTO.BookRequest import BookRequest
from sqlalchemy.orm import relationship
from BDD.BorrowDAO import Borrow


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    borrows = relationship(Borrow, back_populates='book')

    def from_book_request(request: BookRequest):
        return Book(title=request.title, author=request.author)