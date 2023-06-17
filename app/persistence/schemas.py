from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class CallRecord(Base):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True, index=True)
    caller = Column(String, nullable=False)
    word_count = Column(Integer, nullable=False)
    call_started_at = Column(DateTime, nullable=False)
    call_ended_at = Column(DateTime, nullable=False)


# Base.metadata.create_all(engine)
