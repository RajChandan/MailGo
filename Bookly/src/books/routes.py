from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
#from schemas import Book,BookUpdateModel,BookCreateModel
from src.books.schemas import Book,BookUpdateModel,BookCreateModel
from typing import List
from typing import Optional
from pydantic import BaseModel


book_router = APIRouter()

@book_router.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        "title" : book_data.title,
        "author" : book_data.author
    }


@book_router.get('/')
async def read_root():
    return {"message":"Hello World"}

@book_router.get('/greet/')
async def greet_name(name:Optional[str]="User",age:int=0) -> dict:
    return {"message":f"Hello {name} Age : {age}"}