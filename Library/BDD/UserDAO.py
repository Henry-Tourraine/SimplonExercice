from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from .Context import Base
from DTO.SignupForm import SignupForm
from DTO.LoginForm import LoginForm
from DTO.UserDTO import UserDTO
from BDD.BorrowDAO import Borrow


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    pwd = Column(String)

    borrows = relationship(Borrow, back_populates='user')

    def to_dto(self):
        return UserDTO(id=self.id, name=self.name, email=self.email, pwd=self.pwd)


    def from_signup_form(form: SignupForm):
        return User(name=form.name, email=form.email, pwd=form.pwd)
    