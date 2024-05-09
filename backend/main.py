from fastapi import FastAPI
from core.config import settings
from core import base_router
from fastapi.middleware.cors import CORSMiddleware
#from db.base import Base

app = FastAPI(
    title= settings.PROJECT_TITLE,
    description="CRUD operations apis",
    terms_of_service="http://www.google.com",
    contact={
        "developer name":"Amol Shewalkar",
        "email":"amol.s@amazatic.com"
    },
    license_info={
        "name":"ABC",
        "url":"http://www.google.com"
    },
    #openapi_url="" (define custom url for swagger(url docs))
)

origins = [
    #"http://localhost:3000"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


app.include_router(base_router.api_router)

