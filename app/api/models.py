from typing import List
from pydantic import BaseModel
from datetime import datetime


class HealthResponse(BaseModel):
    status: str


class PagingDTO(BaseModel):
    offset: int
    limit: int
    total: int


class CallRecordDTO(BaseModel):
    id: int
    caller: str
    word_count: int
    call_started_at: datetime
    call_ended_at: datetime

    class Config:
        orm_mode = True


class CallRecordPaginatedResponse(BaseModel):
    results: List[CallRecordDTO]
    paging: PagingDTO
