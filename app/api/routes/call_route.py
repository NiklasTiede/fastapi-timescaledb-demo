from fastapi import APIRouter, HTTPException, Query, Depends, Security
from sqlalchemy.orm import Session

from datetime import datetime

from starlette import status

from app.api.models import CallRecordPaginatedResponse
from app.middleware.api_key_auth import get_api_key
from app.persistence.session import get_db
from app.services.call_service import CallService

router = APIRouter()


@router.get("/call_records",
            status_code=status.HTTP_200_OK,
            response_model=CallRecordPaginatedResponse,
            tags=["Call Data"],
            dependencies=[Depends(get_api_key)])
def read_records(
        start_date: datetime = Query(..., title="Start Date", description="The start date of the filter", alias="start_date"),
        end_date: datetime = Query(..., title="End Date", description="The end date of the filter", alias="end_date"),
        offset: int = Query(0, title="Offset", description="The offset for paging"),
        limit: int = Query(100, title="Limit", description="The limit for paging"),
        db: Session = Depends(get_db)
):
    results = CallService.get_records(db, start_date, end_date, offset, limit)

    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Records not found")
    return results
