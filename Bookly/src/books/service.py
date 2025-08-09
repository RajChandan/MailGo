from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .models import Book


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book(self, session: AsyncSession, book_uid: str):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        book = result.one_or_none()
        if not book:
            raise ValueError(f"Book with uid {book_uid} not found")
        return book

    async def book_create(self, session: AsyncSession, book_data: BookCreateModel):
        pass

    async def book_update(
        self, session: AsyncSession, book_uid: str, update_data: BookUpdateModel
    ):
        pass

    async def book_delete(self, session: AsyncSession, book_uid: str):
        pass
