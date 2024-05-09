from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db
from .models import User

def get_user_by_email(email:str, db:Session=Depends(get_db)):
    return db.query(User).filter(User.email == email).first()