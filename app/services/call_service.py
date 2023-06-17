from datetime import datetime

from sqlalchemy.orm import Session

from app.persistence.repository.call_repository import CallRepository


class CallService:

    @staticmethod
    def get_records(db: Session, start_date: datetime, end_date: datetime, offset: int, limit: int):
        return CallRepository.get_records(db, start_date, end_date, offset, limit)
