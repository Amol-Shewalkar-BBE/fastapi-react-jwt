# app/db/relationships.py
from sqlalchemy.orm import relationship
from user.models import User
from blog.models import Blog
from .base_class import Base

def configure_relationships():
    # blog and user realtionship
    User.blogs = relationship('Blog', back_populates='author')
    Blog.author = relationship('User', back_populates='blogs')
    Base.prepare()