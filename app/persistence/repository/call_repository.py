from datetime import datetime

from sqlalchemy.orm import Session

from app.persistence.schemas import CallRecord
from app.api.models import CallRecordDTO, PagingDTO, CallRecordPaginatedResponse


class CallRepository:

    @staticmethod
    def get_records(db: Session, start_date: datetime, end_date: datetime, offset: int, limit: int) -> CallRecordPaginatedResponse:
        records = (
            db.query(CallRecord)
            .filter(
                CallRecord.call_started_at >= start_date,
                CallRecord.call_started_at <= end_date
            )
            .offset(offset)
            .limit(limit)
            .all()
        )
        total = (
            db.query(CallRecord)
            .filter(
                CallRecord.call_started_at >= start_date,
                CallRecord.call_started_at <= end_date
            )
            .count()
        )
        return CallRecordPaginatedResponse(
            results=[CallRecordDTO.from_orm(record) for record in records],
            paging=PagingDTO(limit=limit, offset=offset, total=total)
        )

