from fastapi import FastAPI
from app.routes.match import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API Running"}

app.include_router(router)