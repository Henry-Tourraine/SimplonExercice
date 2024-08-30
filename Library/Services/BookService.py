from Repositories.BookRepository import BookRepository
from BDD.BookDAO import Book
from DTO.BookRequest import BookRequest


class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def create(self, book: BookRequest)->Book:
        already_exists = self.repo.get_one_by("title", book.title)
        if already_exists:
            return None
        return self.repo.create(Book.from_book_request(book))
    

    def get_one_by_id(self, id: int):
        return self.repo.get_one_by("id", id)


    def get_many(self):
        return self.repo.get_all(skip=0, limit=1000)