import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# CONFIG
# ---------------------------
REQUIRED_SKILLS = ["python", "sql"]
SKILLS_DB = ["python", "sql", "excel", "power bi", "machine learning"]

# ---------------------------
# CLEAN TEXT
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# ---------------------------
# SKILL EXTRACTION
# ---------------------------
def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill in text]

# ---------------------------
# EXPERIENCE EXTRACTION
# ---------------------------
def extract_experience(text):
    match = re.search(r'(\d+(\.\d+)?)\s*(years|year)', text.lower())
    if match:
        return float(match.group(1))
    return 0

# ---------------------------
# CORE FUNCTION (API READY)
# ---------------------------
def screen_resumes_api(resumes, job_description):

    clean_resumes = [clean_text(r) for r in resumes]
    clean_jd = clean_text(job_description)

    docs = clean_resumes + [clean_jd]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(docs)

    similarity_scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

    results = []

    for i in range(len(resumes)):

        skills = extract_skills(clean_resumes[i])
        experience = extract_experience(resumes[i])

        skill_score = len(skills) / len(SKILLS_DB)
        exp_score = min(experience / 2, 1)

        final_score = (
            0.5 * similarity_scores[i] +
            0.3 * skill_score +
            0.2 * exp_score
        )

        missing = [s for s in REQUIRED_SKILLS if s not in skills]

        decision = (
            "Rejected" if missing else
            "Shortlisted" if final_score >= 0.5 else
            "Rejected"
        )

        results.append({
            "similarity_score": round(float(similarity_scores[i]), 3),
            "skill_score": round(skill_score, 3),
            "experience": experience,
            "final_score": round(final_score, 3),
            "skills": skills,
            "missing_skills": missing,
            "decision": decision
        })

    results.sort(key=lambda x: x["final_score"], reverse=True)

    return results