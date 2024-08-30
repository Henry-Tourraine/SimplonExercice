from fastapi import FastAPI
from BDD.Context import Base, engine
from Controllers import user_router, borrow_router, book_router
from Middlewares import handle_error
from Repositories import UserRepository
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer


# BDD
Base.metadata.create_all(bind=engine)


load_dotenv()

app = FastAPI()


# Controllers
app.include_router(book_router)
app.include_router(user_router)
app.include_router(borrow_router)

# Middlewares
app.middleware("http")(handle_error)



@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}