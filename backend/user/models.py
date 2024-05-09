from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    is_active = Column(Boolean, default=False)
    #blogs = relationship('blog.models.Blog', back_populates='author', lazy='dynamic')
    
    