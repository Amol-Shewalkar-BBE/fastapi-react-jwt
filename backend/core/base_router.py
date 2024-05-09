from fastapi import APIRouter
from user import router_user
from blog import router_blog

api_router = APIRouter()


api_router.include_router(router_user.router,tags=['users'])
api_router.include_router(router_blog.router, prefix='/blogs', tags=['blogs'])