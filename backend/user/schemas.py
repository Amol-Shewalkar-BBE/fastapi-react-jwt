from pydantic import BaseModel, EmailStr, Field
from fastapi import Depends, HTTPException
from sqlalchemy import Enum
from typing import Optional
from datetime import datetime



class UserCreate(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    password : str = Field(..., min_length=4)
    role : str
    

class UserShow(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    password : str = Field(..., min_length=4)
    role : str

    class Config():
        from_attributes=True

class UserEmail(BaseModel):
    id:int
    email:str
    role:str

class UserDetails(BaseModel):
    id:int
    first_name : str
    last_name : str
    email : EmailStr
    role : str

    class Config():
        from_attributes = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None