from fastapi import APIRouter, Depends, HTTPException, status
from Crypto import get_current_user, UserClaim
from Services.BorrowService import BorrowService
from DTO.BorrowForm import BorrowForm
from DTO.UserDTO import UserDTO


borrow_router = APIRouter(
    prefix="/borrows",
    tags=["borrows"],
    responses={404: {"description": "Not found"}}
)

service = BorrowService()


@borrow_router.post("/{book_id}")
async def post_create(book_id: int, user: UserDTO = Depends(get_current_user)):
    """
    User borrows a book if not already borrowed.
    """
    borrow = service.create(BorrowForm(user_id=user.id, book_id=book_id))
    if borrow:
        return borrow
    raise HTTPException(400, "Book already borrowed")


@borrow_router.get("/current/all")
def get_all_current_borrowed_books(user: UserClaim = Depends(get_current_user)):
    """
    Gets all pending borrowings for a user.
    """
    return service.get_current_borrows(user.id)


@borrow_router.get("/all")
def get_all_borrowed_books(user: UserClaim = Depends(get_current_user)):
    """
    Gets all user's borrowing history.
    """
    return service.get_all_borrows(user.id)


@borrow_router.get("/book/available/{id}")
def is_available(id: int, user: UserClaim = Depends(get_current_user)):
    """
    Checks if a borrowing is not pending for a book.
    """
    return service.is_book_available(id)