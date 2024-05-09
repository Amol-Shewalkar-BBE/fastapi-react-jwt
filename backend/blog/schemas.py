from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlogCreate(BaseModel):
    title:str
    content:str
    auther_id:int


class BlogShow(BaseModel):
    id:int
    title:str
    content:str
    auther_id:int
    created_at:Optional[datetime]= None
    updated_at:Optional[datetime]=None

    class Config():
        orm_mode=True