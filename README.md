# RATE MY RESUME USING ML & NLP
> **_Upload a resume. Match it against company requirements. Get an eligibility score with actionable insights._**

**Rate My Resume** is a resume screening and scoring web application that uses **Machine Learning + Natural Language Processing (NLP)** techniques to evaluate how well a candidate’s resume matches **company/job requirement datasets**. Users can upload a resume, select one or more companies, and instantly receive an **eligibility percentage**, **graphical results**, and **improvement suggestions**.

This project was developed as a **B.Tech CSE Mini Project (2020–2021)**.

---

## Why This Project?
Many candidates are filtered out early due to **keyword mismatch**, missing critical skills, or not presenting experience in a way that aligns with company expectations. Recruiters and ATS tools often look for specific terms related to:
- Skills and tools (Python, SQL, Cloud, etc.)
- Technical keywords (data structures, ML, NLP, testing, etc.)
- Projects, internships, achievements, certifications
- Domain requirements

This project helps candidates **self-check** their resume alignment before applying, saving time and improving chances of shortlisting.

---

## What It Does
At a high level, the system:
1. Allows users to **Register/Login**
2. Lets users **upload a resume (.docx)**
3. Provides a list of companies (or job profiles) with **checkbox selection**
4. Extracts resume content and performs **text preprocessing**
5. Compares resume terms and phrases against **company requirements**
6. Calculates **match percentages**
7. Displays results using a **bar graph**
8. Shows a **result page** with eligibility message + suggestions

---

## Key Features

### 1) User Authentication (MySQL)
- User registration and login
- Stores user login data in **MySQL**
- Prevents duplicate registrations using email/unique fields
- Basic validation for incorrect credentials

### 2) Resume Upload + Multi-Company Evaluation
- Upload resume in **.docx format**
- Select multiple companies using checkboxes
- Generates a score for each selected company
- Useful for comparing which company/job requirement your resume matches best

### 3) NLP-Based Text Processing
The resume is cleaned and processed to improve matching accuracy:
- Text extraction using **docx2txt**
- Tokenization using **NLTK**
- Stopword removal
- N-gram generation (**bigrams/trigrams**) to capture multi-word skills like:
  - “machine learning”
  - “data analysis”
  - “deep learning”
  - “project management”

### 4) Matching & Scoring
- Uses a company requirement dataset (skills/keywords)
- Compares extracted resume tokens and phrases with requirement terms
- Computes a match score / eligibility percentage per company
- Produces structured output for graph + message page

### 5) Results Visualization + Suggestions
- **Matplotlib bar graph** to show eligibility scores
- Result message page:
  - If score is high → “eligible” message
  - If score is low → improvement guidance (add missing skills, strengthen sections)

---

## User Roles
### Candidate (User)
- Register/Login
- Upload resume
- Select company checkbox(es)
- View score + graph + suggestions

*(Optional future role: Admin to manage company requirement datasets)*

---

## Pages / Screens (Modules)
### Frontend Pages
- Welcome Page
- Register Page
- Login Page
- Upload Resume Page (with checkbox company selection)
- Result Page (bar graph + message)

### Backend Modules
- File upload handler
- Resume text extraction
- NLP preprocessing pipeline
- Matching + scoring engine
- Graph generation module
- Database connection module (MySQL)

---

## Tech Stack
- **Backend**: Python
- **Framework**: Flask
- **NLP**: NLTK
- **Visualization**: Matplotlib
- **Frontend**: HTML, CSS
- **Database**: MySQL (MySQL Workbench)
- **Resume Parsing**: docx2txt

---

## System Architecture (Simple View)

```
User (Browser)
|
|  Upload Resume + Select Companies
v
Flask Web App (Routes + Logic)
|
|  Extract Text -> Clean -> Tokenize -> N-grams
v
NLP Processing (NLTK + docx2txt)
|
|  Compare with Requirement Datasets
v
Scoring Engine
|
|  Generate Graph + Message
v
Results Page (Bar Graph + Eligibility Suggestions)
|
v
MySQL (Stores user login info)
```

---

## Data Model (Database)
### MySQL: `login`
Table: `logininfo`
- `id` (primary key)
- `name`
- `email`
- `password`

> Note: For production, passwords should be stored as **hashed values**, not plain text.

---

## Setup and Installation

### Prerequisites
- Python 3.x
- MySQL Server + MySQL Workbench
- pip (Python package manager)

### 1) Clone the Repository
```bash
git clone <your-repo-url>
cd <project-folder>
````

### 2) Create Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3) Install Dependencies

If your repo has `requirements.txt`:

```bash
pip install -r requirements.txt
```

If not, install typical packages:

```bash
pip install flask nltk numpy matplotlib docx2txt
pip install mysqlclient  # OR flask-mysqldb depending on your code
```

### 4) NLTK Setup (First Time)

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 5) Configure MySQL

Create DB and table:

```sql
CREATE DATABASE login;

USE login;

CREATE TABLE logininfo (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(100)
);
```

### 6) Update DB Credentials

In your Flask config file (or `app.py`), set:

* host
* user
* password
* database = `login`

---

## How to Run

```bash
python app.py
```

Then open:

* `http://localhost:5000`

---

## Testing

Testing approaches covered:

* **Black Box Testing** (UI input/output validation)
* **White Box Testing** (logic-level testing)
* **Grey Box Testing** (combined approach)

Testing levels:

* Unit testing
* Integration testing
* System testing
* User Acceptance Testing

Example test cases:

* Register with an already registered email
* Login with wrong password
* Upload file without selecting a company
* Upload unsupported format
* Multiple checkbox selection scoring

---

## Results (What You See)

* A bar graph showing eligibility scores for selected companies
* A message page explaining:

  * Whether you are eligible / close to eligible
  * What to improve (missing skills/keywords/sections)

---

## Future Enhancements

* Support PDF resumes with reliable extraction
* Use semantic similarity (Word2Vec/BERT embeddings) instead of strict keyword matching
* Admin dashboard for maintaining company datasets
* Add section-wise scoring (Skills / Projects / Internships / Certifications)
* Provide recommended keywords based on target company/job
* Export results as a downloadable report (PDF)
* Add ATS-friendly formatting checks

---

## Contributors

**Mini Project Team**

* Kollapudi Bindu Sri Nagavalli
* Komatlapalli Venkata Naga Sri
* Supraja Naraharisetty
* Mucherla Sai Sri Lakshmi Chaitanya
* Mancheela Neeraja Rajeshwari



