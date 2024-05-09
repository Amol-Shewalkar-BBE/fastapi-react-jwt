from fastapi import APIRouter, status, Depends, HTTPException
from .models import User
from .schemas import (UserCreate, UserShow,UserDetails, Token, UserEmail)
from db.session import get_db
from sqlalchemy.orm import Session
from core.hashing import Hasher
from .utils import get_user_by_email
from fastapi.security import OAuth2PasswordRequestForm
from .auth import (create_access_token)
from core.hashing import Hasher
import json
from .auth import get_current_user
from db.permissions import RoleChecker

router = APIRouter()



@router.post('/signup', response_model=UserShow, status_code=status.HTTP_201_CREATED)
async def CreateUser(user: UserCreate, db: Session = Depends(get_db)):
    
    if get_user_by_email(user.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with email already exist")
    
    hashed_password = Hasher.get_password_hash(user.password)
    user_data = user.dict()
    user_data['password']=hashed_password
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user


# router to user login
@router.post('/login', response_model=Token)
async def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username")
    if not Hasher.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": user.email})
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}


# fetching all user
@router.get('/', response_model=list[UserDetails], dependencies=[Depends(RoleChecker(['admin']))])
async def get_all_user(db:Session=Depends(get_db), user:UserEmail =Depends(get_current_user)):
    users = db.query(User).all()
    return users



