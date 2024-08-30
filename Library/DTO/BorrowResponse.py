from pydantic import BaseModel


class BorrowResponse(BaseModel):
    title: str
    author: str