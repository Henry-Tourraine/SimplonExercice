from pydantic import BaseModel


class SignupForm(BaseModel):
    name: str
    email: str
    pwd: str