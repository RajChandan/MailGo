from sqlmodel.ext.asyncio.session import AsyncSession


class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass
