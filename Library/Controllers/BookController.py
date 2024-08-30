from fastapi import APIRouter, Depends, HTTPException, status
from Crypto import get_current_user, UserClaim
from DTO.SignupForm import SignupForm
from Services.BookService import BookService
from DTO.BookRequest import BookRequest


book_router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}}
)

service = BookService()


@book_router.post("/create")
def post_create(request: BookRequest, user: UserClaim = Depends(get_current_user)):
    """
    Creates a book. (title must be unique)
    """
    u = service.create(request)
    if u:
        return u
    else:
        raise HTTPException(status_code=400, detail="Item already exists")

@book_router.get("/all")
def get_all(user: UserClaim = Depends(get_current_user)):
    """
    Gets all existing books.
    """
    return service.get_many()
