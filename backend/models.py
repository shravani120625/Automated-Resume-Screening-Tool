import uuid
from sqlalchemy import Column, String, Float, ForeignKey, UniqueConstraint
from db.database import Base

def generate_id():
    return str(uuid.uuid4())


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    min_experience = Column(Float)


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(String, primary_key=True, default=generate_id)

    candidate_id = Column(String, index=True)
    job_id = Column(String, ForeignKey("jobs.id"))

    skills = Column(String)
    experience = Column(Float)

    __table_args__ = (
        UniqueConstraint("candidate_id", "job_id"),
    )