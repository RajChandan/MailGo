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
            return None
        return book

    async def book_create(self, session: AsyncSession, book_data: BookCreateModel):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)

        await session.commit()
        return new_book

    async def book_update(
        self, session: AsyncSession, book_uid: str, update_data: BookUpdateModel
    ):
        book_to_update = self.get_book(session, book_uid)
        if book_to_update:
            book_to_update_dict = update_data.model_dump()
            for k, v in book_to_update_dict.items():
                setattr(book_to_update, k, v)

            await session.commit()
            return book_to_update
        else:
            return None

    async def book_delete(self, session: AsyncSession, book_uid: str):
        book_to_delete = self.get_book(session, book_uid)
        if book_to_delete:
            await session.delete(book_to_delete)
            await session.commit()
            return book_to_delete
        else:
            return None
