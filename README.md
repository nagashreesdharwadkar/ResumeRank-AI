<<<<<<< HEAD
# ResumeRank AI

ResumeRank AI is an AI-powered ATS (Applicant Tracking System) Resume Analyzer that evaluates resumes against job descriptions and provides actionable feedback to improve job application success rates.

## Features

* ATS Resume Scoring
* Resume Parsing (PDF, DOC, DOCX)
* Job Description Matching
* Skill Validation
* Keyword Analysis
* Semantic Similarity Analysis
* AI-Powered Feedback using Groq LLM
* Resume Improvement Suggestions
* User Authentication (Email & Google OAuth)
* Analysis History Tracking
* PDF Report Generation

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Python

### NLP & AI

* spaCy
* Sentence Transformers
* Groq API (Llama 3)

### Database & Authentication

* Supabase

### Report Generation

* FPDF
* Jinja2

## Project Structure

```text
ResumeRank_AI/
│
├── backend/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── frontend/
│   ├── components/
│   ├── services/
│   ├── views/
│   └── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .env.example
```

## Installation

### Clone Repository

```bash
git clone https://github.com/nagashreesdharwadkar/ResumeRank_AI.git
cd ResumeRank_AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file inside the backend folder:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_KEY=your_supabase_service_role_key
AUTH_REDIRECT_URL=http://localhost:8501
```

## Running the Backend

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Backend URL:

```text
http://127.0.0.1:8000
```

## Running the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

## Workflow

1. User uploads resume.
2. Resume is parsed and analyzed.
3. ATS score is calculated.
4. Skills are validated.
5. Resume is matched against job description.
6. AI generates improvement suggestions.
7. Results and reports are displayed.

## Future Enhancements

* Resume Builder
* Interview Question Generator
* Multiple Resume Comparison
* Job Recommendation Engine
* Resume Templates Marketplace

## Author

Nagashree S D

Information Science Engineering Student

SDMCET Dharwad
=======
# ResumeRank_AI
>>>>>>> 875a714271b2b125bb665d7ee0dc523156954733
