from Repositories.UserRepository import UserRepository
from DTO import LoginForm, SignupForm
from Crypto.Encryption import verify_password, hash_password
from BDD.UserDAO import User
from Crypto.Token import create_jwt
from datetime import timedelta


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def hide_pwd(self, user: User):
        user.pwd = "*****"
        return user

    def signup(self, signup_form: SignupForm):
        signup_form.pwd = hash_password(signup_form.pwd)
        user = User.from_signup_form(signup_form)
        user = self.repo.create(user)
        user = self.hide_pwd(user)
        return user

    def login(self, login_form: LoginForm):
        user = self.repo.get_one_by("email", login_form.email)
        if user:
            if verify_password(login_form.pwd, user.pwd):
                return create_jwt(user.id, timedelta(hours=5))
        return None