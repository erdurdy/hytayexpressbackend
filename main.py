from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.api import router as api_router
from src.database import Base, engine, metadata


app = FastAPI(
    title="Backend"
)

Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:5000",
    "http://192.168.1.39",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)