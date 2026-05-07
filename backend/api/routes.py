from fastapi import APIRouter, UploadFile, Form, Depends, File
from sqlalchemy.orm import Session
import uuid
import json
from collections import defaultdict

from db.database import SessionLocal
from models import Job, Resume
from api.utils import clean_text, extract_skills, extract_experience, compute_score
from pydantic import BaseModel
from typing import List
import pdfplumber
import io

router = APIRouter()

class JobInput(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    min_experience: float = 1.0
# -----------------------
# DB Dependency
# -----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class JobInput(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    min_experience: float = 1.0

# -----------------------
# CREATE JOB
# -----------------------
@router.post("/job")
def create_job(job: JobInput, db: Session = Depends(get_db)):
    job_id = str(uuid.uuid4())

    db_job = Job(
        id=job_id,
        title=job.title,
        description=job.description,
        min_experience=job.min_experience
    )

    db.add(db_job)
    db.commit()

    return {"job_id": job_id}

# -----------------------
# UPLOAD RESUME (FIXED)
# -----------------------
@router.post("/upload/{job_id}")
async def upload_resume(
    job_id: str,
    candidate_id: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    contents = await file.read()

    if file.filename.endswith(".pdf"):

        pdf = pdfplumber.open(io.BytesIO(contents))

        text = ""

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    else:

        text = contents.decode("utf-8", errors="ignore")

    cleaned = clean_text(text)

    skills = extract_skills(cleaned)

    exp = extract_experience(text)

    existing = db.query(Resume).filter(
        Resume.candidate_id == candidate_id,
        Resume.job_id == job_id
    ).first()

    if existing:
        return {"message": "Resume already uploaded"}

    db_resume = Resume(
        id=str(uuid.uuid4()),
        candidate_id=candidate_id,
        job_id=job_id,
        skills=json.dumps(skills),
        experience=exp
    )

    db.add(db_resume)

    db.commit()

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "skills": skills,
        "experience": exp
    }
# -----------------------
# RANKING
# -----------------------
# -----------------------
# RANK CANDIDATES
# -----------------------
@router.get("/rank/{job_id}")
def rank(job_id: str, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    resumes = db.query(Resume).filter(
        Resume.job_id == job_id
    ).all()

    results = []

    for r in resumes:

        skills = json.loads(r.skills)

        resume_text = " ".join(skills)

        score = compute_score(
            skills,
            r.experience,
            resume_text,
            job.min_experience,
            job.description
        )

        results.append({
            "candidate_id": r.candidate_id,
            "score": round(score, 2),
            "decision": (
                "Shortlisted"
                if score >= 0.6
                else "Rejected"
            )
        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "job_id": job_id,
        "total_candidates": len(results),
        "results": results
    }