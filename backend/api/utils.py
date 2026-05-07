import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined skill database (IMPORTANT)
SKILLS_DB = ["python", "sql", "excel", "power bi", "machine learning"]


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]


def extract_experience(text):
    match = re.search(r'(\d+(\.\d+)?)\s*(years|year)', text.lower())
    return float(match.group(1)) if match else 0


def text_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, job_text])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]


def compute_score(skills, experience, resume_text, job_exp, job_text):

    # FIX: proper required skills handling
    required_skills = set(SKILLS_DB)

    skill_score = len(set(skills) & required_skills) / max(len(required_skills), 1)

    exp_score = min(experience / max(job_exp, 1), 1.2)

    similarity_score = text_similarity(resume_text, job_text)

    final_score = (
        0.5 * skill_score +
        0.3 * exp_score +
        0.2 * similarity_score
    )

    return round(final_score, 2)