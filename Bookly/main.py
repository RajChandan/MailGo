from fastapi import FastAPI, Header
from src.books.routes import book_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting ...")
    yield
    print(f"server has stopped.")


version = "v1"
app = FastAPI(title="bookly", version=version, lifespan=life_span)

app.include_router(book_router, prefix=f"/api/{version}/books")
