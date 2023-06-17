from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader

import os


API_KEYS = [
    os.getenv("API_KEY", default="KaB00Mer")
]

api_key_header = APIKeyHeader(name="api-key", auto_error=False)


def get_api_key(
        api_key_h: str = Security(api_key_header),
) -> str:
    if api_key_h in API_KEYS:
        return api_key_h
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
