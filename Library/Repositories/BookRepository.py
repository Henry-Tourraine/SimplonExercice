from .BaseRepository import BaseRepository
from BDD.BookDAO import Book


class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)
    