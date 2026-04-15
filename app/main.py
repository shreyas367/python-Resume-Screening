from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.match import router

app = FastAPI()

# 🚀 Add CORS middleware to allow requests from your Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can restrict this to your Vercel URL later)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def home():
    return {"message": "ML API Running"}

app.include_router(router)