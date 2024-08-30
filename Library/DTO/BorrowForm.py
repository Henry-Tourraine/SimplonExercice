from pydantic import BaseModel


class BorrowForm(BaseModel):
    user_id: int
    book_id: int