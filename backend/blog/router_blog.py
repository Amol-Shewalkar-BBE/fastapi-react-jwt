from fastapi import Depends, HTTPException, APIRouter
from .schemas import *
from sqlalchemy.orm import Session
from .queries import *
from db.session import get_db
from user.models import User
from user.auth import get_current_user
from user.schemas import UserEmail, UserDetails
from db.permissions import RoleChecker

router = APIRouter()

@router.get('/', response_model=list[BlogShow], dependencies=[Depends(RoleChecker(['admin','customer','editor']))])
async def get_all_blogs(db:Session = Depends(get_db), user:UserDetails = Depends(get_current_user)):
    return get_all(db)

@router.get('/{id}', response_model=BlogShow, dependencies=[Depends(RoleChecker(['admin','customer','editor']))])
async def get_blog(id:int, db:Session =Depends(get_db), user:UserEmail =Depends(get_current_user)):
    return retrive(id,db)

@router.post('/', response_model=BlogCreate, dependencies=[Depends(RoleChecker(['customer']))])
async def create_blog(request:BlogCreate, db:Session =Depends(get_db), user:UserEmail =Depends(get_current_user)):
    request.auther_id = user.id
    return create(request,db)

@router.put('/{id}', dependencies=[Depends(RoleChecker(['customer','editor']))])
async def update_blog(id:int,request:BlogCreate, db:Session =Depends(get_db), user:UserEmail =Depends(get_current_user)):
    print(request)
    request.auther_id = user.id
    return update(id,request,db)

@router.delete('/{id}', dependencies=[Depends(RoleChecker(['admin','customer']))])
async def delete_blog(id:int, db:Session =Depends(get_db), user:UserEmail =Depends(get_current_user)):
    return destroy(id,db)