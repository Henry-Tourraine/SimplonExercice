
from pydantic import BaseModel
from fastapi import Request, HTTPException, Depends
from DTO.UserDTO import UserDTO
from fastapi.security import OAuth2PasswordBearer
from Crypto.Token import decode_jwt
from Repositories.UserRepository import UserRepository
from datetime import datetime


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    authorization = token
    if authorization is not None:
        print(f"jwt {authorization}")
        jwt = decode_jwt(authorization)
        try:
            user = UserRepository().get_one_by("id", jwt["id"])
            print(f"auth middleware {user}")

            if user and jwt["exp"] > datetime.now().timestamp() :
                return user

        except Exception as e:
            print(f"===========================================>>>>>>>>>>>>>>>>>>> get current user {e}")
            return None


class UserClaim(BaseModel):
    jwt: str
    user: UserDTO

