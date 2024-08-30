
from Repositories.BorrowRepository import BorrowRepository
from BDD.BorrowDAO import Borrow
from DTO.BorrowForm import BorrowForm
from .BookService import BookService
from BDD.utils import Filter
from datetime import datetime

class BorrowService:
    def __init__(self):
        self.repo = BorrowRepository()
        self.bookService = BookService()


    def create(self, form: BorrowForm):
        if self.is_book_available(form.book_id):
            borrow = Borrow.from_borrow_form(form)
            return self.repo.create(borrow)
        return None


    def is_book_available(self, book_id):
        borrows = self.repo.get_many_by("book_id", book_id)
        for borrow in borrows:
            print(borrow.end)
            if datetime.now().timestamp() < borrow.end:
                return False
        return True


    def get_current_borrows(self, user_id: int):
        results = []
        borrows = self.repo.get_many_by_many([Filter("user_id", "eq", user_id), Filter("end", "gt", datetime.now().timestamp())], options=True)
        for borrow in borrows:
            print(f"borrow #{borrow.id} {borrow.book_id}")
            print(borrow)
            borrow.book = borrow.book
            borrow.user.pwd = "****"
        return borrows



    def get_all_borrows(self, user_id: int):
        borrows =  self.repo.get_many_by("user_id", user_id, options=True)
        for borrow in borrows:
            borrow.book = borrow.book
            borrow.user.pwd = "****"
        return borrows