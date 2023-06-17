from fastapi import FastAPI

from app.api.models import HealthResponse
from app.api.routes.call_route import router as call_route

app = FastAPI()

app.include_router(call_route, prefix="/api/v1")


@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")
