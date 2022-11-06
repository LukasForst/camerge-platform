from fastapi import FastAPI

from backend.api.calendar import router as calendar_router
from backend.api.service import router as service_router

app = FastAPI()
app.include_router(calendar_router)
app.include_router(service_router)
