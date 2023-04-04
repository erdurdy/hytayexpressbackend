from fastapi import FastAPI

from routes.api import router as api_router


app = FastAPI(
    title="Backend"
)


app.include_router(api_router)