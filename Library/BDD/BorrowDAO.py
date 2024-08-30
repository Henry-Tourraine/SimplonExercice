from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from DTO.BorrowForm import BorrowForm
from .Context import Base
from datetime import timedelta, datetime

class Borrow(Base):
    __tablename__ = 'borrows'
    
    id = Column(Integer, primary_key=True)
    start =  Column(Integer, default=datetime.now().timestamp())
    end =  Column(Integer, default=(datetime.now() + timedelta(minutes=2)).timestamp())
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    user = relationship('User', back_populates='borrows')
    book = relationship('Book', back_populates='borrows')

    def from_borrow_form(form: BorrowForm):
        return Borrow(user_id=form.user_id, book_id=form.book_id)