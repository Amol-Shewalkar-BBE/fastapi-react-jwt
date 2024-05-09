from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Blog(Base):
    id =  Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    auther_id = Column(Integer, ForeignKey('user.id'))
    
    