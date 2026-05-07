
````md
1. AI Resume Screening System

An AI-powered Resume Screening and Candidate Ranking platform built using **FastAPI**, **Next.js**, **TailwindCSS**, and **SQLite**.  
The system automates candidate evaluation by analyzing resumes, extracting skills & experience, and ranking applicants based on job requirements.


2. Features

- Create Job Profiles
- Upload Multiple Candidate Resumes
- Automated Resume Parsing
- AI-based Candidate Ranking
- Interactive Analytics Dashboard
- Search & Filter Candidates
- Leaderboard View
- CSV Export Functionality
- Responsive Modern UI


3. Tech Stack

**Frontend**
- Next.js 16
- TypeScript
- TailwindCSS
- Axios
- Recharts

**Backend**
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn



4. System Architecture

```text
Frontend (Next.js)
        │
        ▼
FastAPI REST APIs
        │
        ▼
SQLite Database
````


5. Project Structure

```bash
Automated-Resume-Screening-Tool/
│
├── backend/
│   ├── api/
│   │   ├── app.py
│   │   ├── routes.py
│   │   └── utils.py
│   │
│   ├── db/
│   │   └── database.py
│   │
│   ├── models.py
│   ├── init_db.py
│   └── __pycache__/
│
├── frontend/
│   ├── app/
│   │   └── page.tsxs
│   │
│   ├── public/
│   ├── lib/
│   ├── package.json
│   ├── tsconfig.json
│   └── next.config.ts
│
├── images/
│   ├── dashboard.png
│   ├── analytics.png
│   ├── upload.png
│   └── leaderboard.png
│
├── outputs/
│   ├── results.csv
│   └── final_report.csv
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```



6. Installation & Setup

  1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git
```

  2.Backend Setup

   Move to Backend Directory

```bash
cd backend
```

  3.Create Virtual Environment

  Windows

```bash
python -m venv venv
venv\Scripts\activate
```

  Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

 4.Install Dependencies

```bash
pip install -r requirements.txt
```

---

 5.Start Backend Server

```bash
uvicorn api.app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

 6.Frontend Setup

 Move to Frontend Directory

```bash
cd frontend
```

---

 7.Install Dependencies

```bash
npm install
```

---

8.Install Additional Packages

```bash
npm install axios recharts file-saver
```

---

9.Run Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```


7. API Endpoints

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| POST   | `/job`             | Create Job      |
| POST   | `/upload/{job_id}` | Upload Resume   |
| GET    | `/rank/{job_id}`   | Rank Candidates |



8. Workflow

1. Create a Job Description
2. Upload Candidate Resumes
3. Extract Skills & Experience
4. Calculate Candidate Scores
5. Rank Candidates
6. Visualize Analytics



9. Dashboard Features

* Candidate Score Visualization
* AI Match Percentage
* Shortlisted/Rejection Status
* Candidate Search
* Decision Filters
* CSV Export
* Leaderboard Ranking

---

10. Screenshots

Dashboard
![Dashboard](<a. Dashboard.png>)
![Job Create](<b. Job Description.png>)
![upload and result](<c. Upload.png>)

Analytics

![analytics](<d. Analytics.png>)

Leaderboard
![alt text](<e. Shortlisted Table.png>) ![alt text](<f. csv and search.png>)


11. Future Enhancements

* NLP-based Resume Parsing
* PDF & DOCX Resume Support
* JWT Authentication
* Email Notifications
* AI Skill Recommendation
* Cloud Deployment
* Recruiter Admin Panel


12. Author
    Developed by Shravani Hande.
    Github : https://github.com/shravani120625/Automated-Resume-Screening-Tool.git
    Linkedin :https://www.linkedin.com/in/shravani-hande-a443ab331?utm_source=share_via&utm_content=profile&utm_medium=member_android
    




13. License

MIT License

Copyright (c) 2026 Shravani Hande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
```
=======
# Automated-Resume-Screening-Tool
AI-powered Automated Resume Screening System using FastAPI + Next.js that evaluates, ranks, and visualizes candidate resumes based on job requirements using NLP-based scoring and analytics dashboard.
