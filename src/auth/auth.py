from datetime import datetime, timedelta
from typing import Union

import jose
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt
from settings import JWT_Settings


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        return is_valid_token(jwtoken)


oauth2_scheme = JWTBearer()


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT_Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_Settings.SECRET_KEY, algorithm=JWT_Settings.ALGORITHM)
    return encoded_jwt


def is_valid_token(token: str) -> bool:
    try:
        result = jwt.decode(token, JWT_Settings.SECRET_KEY, algorithms=[JWT_Settings.ALGORITHM])
        return True
    except (jwt.ExpiredSignatureError, jose.exceptions.JWTError) as ex:
        print(str(ex))
        return False
    return result
