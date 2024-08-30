from .BaseRepository import BaseRepository
from BDD.UserDAO import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
    