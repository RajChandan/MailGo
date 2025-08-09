from pydantic import BaseModel
import uuid
from datetime import datetime


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    language: str
