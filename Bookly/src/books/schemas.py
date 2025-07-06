from pydantic import BaseModel


class BookCreateModel(BaseModel):
    title : str
    author : str

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    language:str


class BookUpdateModel(BaseModel):
    title:str
    author: str
    publisher: str
    language: str