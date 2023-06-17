from tokenize import String

from faker import Faker
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, DateTime, insert
from sqlalchemy.orm import Session, declarative_base, Mapper

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/postgres"



Base = declarative_base()


class CallRecord(Base):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True, index=True)
    caller = Column(String, nullable=False)
    word_count = Column(Integer, nullable=False)
    call_started_at = Column(DateTime, nullable=False)
    call_ended_at = Column(DateTime, nullable=False)


# Initialize Faker
fake = Faker()

# List of 300 unique names
names = set()
while len(names) < 300:
    names.add(fake.name())

names = list(names)  # Convert back to list for indexing

# Connect to your database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Generate data
start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 1, 1)
total_days = (end_date - start_date).days

data = []
for _ in range(10):
    random_days = random.randint(0, total_days-1)
    random_seconds = random.randint(0, 24*60*60-1)
    call_started_at = start_date + timedelta(days=random_days, seconds=random_seconds)
    call_ended_at = call_started_at + timedelta(minutes=random.randint(1, 60))  # Call duration between 1 and 60 minutes
    word_count = random.randint(30, 300)
    caller = random.choice(names)

    data.append(
        {
            "caller": caller,
            "word_count": word_count,
            "call_started_at": call_started_at,
            "call_ended_at": call_ended_at,
        }
    )

print(data)

# entry = [{
#     'caller': 'Terry Gross',
#     'word_count': 76,
#     'call_started_at': datetime(2019, 8, 8, 10, 10, 34),
#     'call_ended_at': datetime(2019, 8, 8, 10, 18, 34)
# }]

entry = [{
    "caller": "name",
    "word_count": 76,
    "call_started_at": "2023-06-01 09:00:00+00",
    "call_ended_at": "2023-06-01 09:00:00+00"
}]

# Batch insert data
with Session(engine) as session:
    session.execute(insert(CallRecord), entry)
    # session.bulk_insert_mappings(
    #     Mapper[CallRecord],  # Assuming CallRecord is your SQLAlchemy model class
    #     entry
    # )
    session.commit()
