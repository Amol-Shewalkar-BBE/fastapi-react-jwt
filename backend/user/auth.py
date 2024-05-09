import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from core.config import settings
from sqlalchemy.orm import Session
from db.session import get_db
from jwt import PyJWTError
from typing import Dict
from .utils import get_user_by_email
from .schemas import UserDetails
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

# create access token
def create_access_token(data: dict):
    # Convert UserDetails object to dictionary
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire_time})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHUM)
    return encoded_jwt

# verfiy access token
def get_current_user(token:str = Depends(oauth2_scheme), db: Session= Depends(get_db)):
    credentials_exception =  HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid user credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        print(token)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHUM)
        print(payload)
        email = payload.get("sub")
        user = get_user_by_email(email, db)
        if user is None:
            raise credentials_exception
        return user

    except PyJWTError as je:
        print(f"JWTError: {str(je)}")
        raise credentials_exception
    

def get_active_user_principals(user:UserDetails = Depends(get_current_user)):
    user_principals = {
        "email": user.email,
        "role": user.role  # Assuming roles is a property of the User model
        # Add more user principals as needed
    }
    return user_principals