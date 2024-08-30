from fastapi import APIRouter, Depends, HTTPException, status
from Crypto import get_current_user, UserClaim
from Services.UserService import UserService
from DTO.SignupForm import SignupForm
from DTO.LoginForm import LoginForm
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

service = UserService()


@user_router.post("/create")
def post_create(signup_form: SignupForm):
    """
    Creates a user.
    """
    return service.signup(signup_form)


@user_router.post("/login")
def post_create(login_form: LoginForm):
    """
    Log in user.
    """
    return service.login(login_form)


@user_router.post("/token")
def post_create(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Log in route for swagger
    """
    token = service.login(LoginForm(email=form_data.username, pwd=form_data.password))
    return {"access_token": token, "token_type": "bearer"}
