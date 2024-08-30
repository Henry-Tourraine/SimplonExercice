from .BaseRepository import BaseRepository
from BDD.BorrowDAO import Borrow


class BorrowRepository(BaseRepository):
    def __init__(self):
        super().__init__(Borrow)
    