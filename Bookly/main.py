from fastapi import FastAPI,Header
from src.books.routes import book_router

version = "v1"
app = FastAPI(
    title="bookly",
    version=version
)

app.include_router(book_router,prefix=f"/api/{version}/books")








