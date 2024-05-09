from .models import Blog
from sqlalchemy.orm import Session
from .schemas import BlogCreate, BlogShow
from fastapi import HTTPException, Response, status

# fetching all blog objects
def get_all(db:Session):
    blogs=db.query(Blog).all()
    return blogs

# fetching specific blog object
def retrive(id:int,db:Session):
    blog=db.query(Blog).filter(Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    return blog
    

# creating blog object
def create(request:BlogCreate, db:Session):
    blog_data = request.dict()
    new_blog = Blog(**blog_data)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# updating blog object
def update(id:int, request:BlogCreate, db:Session):
    blog=db.query(Blog).filter(Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.update(request.dict())
    db.commit()
    return {'blog is updated succefully'}

# deleting blog object
def destroy(id:int, db:Session):
    blog=db.query(Blog).filter(Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog {id} you want to update doesnot exist")
    blog.delete(synchronize_session=False)    
    db.commit()
    return {'blog is deleted'}