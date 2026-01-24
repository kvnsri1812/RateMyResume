# RATE MY RESUME USING ML & NLP

> ***Upload a resume. Match it against company requirements. Get an eligibility score with insights.***

**Rate My Resume** is a web-based resume screening and scoring system that uses **Machine Learning + Natural Language Processing** concepts to compare an uploaded resume against **company requirement datasets** and generate an **eligibility percentage**, a **bar-graph visualization**, and an improvement message. 

This project was developed as a **Mini Project-I (B.Tech CSE)** at **Shri Vishnu Engineering College for Women**, during the **academic year 2020–2021**. 


## Overview

Many applicants get rejected early because their resumes don’t match the right **keywords and requirements** for the companies they apply to. This project helps candidates **validate and improve** their resume *before* applying by checking alignment with company expectations using NLP-based text processing and scoring. 

Rate My Resume checks the eligibility of the resume against the company requirements and helps users to improve their resume so that they can land in their dream companies. Users need to upload their resume and select the company(s) for which they want to check the eligibility. The eligibility percentage(s) will be displayed as bar graph. At last messages will be to help users to improve their resume.

At a high level, the system:

1. Lets the user **register/login**
2. Accepts a resume upload (docx)
3. Lets the user pick one or more companies via **checkboxes**
4. Extracts and cleans resume text
5. Matches resume keywords/phrases vs company requirement lists
6. Calculates percentages and displays:

   * **bar graph**
   * **eligibility message / suggestions** 


## Key Features

### Authentication

* Register and login functionality
* Stores login data in **MySQL** (login database + logininfo table) 

### Resume Upload + Company Selection

* Upload CV/Resume (docx format)
* Select target companies using checkboxes
* Basic validation (file + at least one company selected) 

### NLP Processing + Matching

* Extract resume text and tokenize using **NLTK**
* Remove stopwords
* Generate bigrams/trigrams for better phrase matching
* Match against company requirement dictionaries (skills, technical skills, etc.)
* Includes additional criteria such as projects/internships/strengths as part of scoring (as described in implementation) 

### Results + Visualization

* Eligibility score/percentages computed per selected company
* **Matplotlib bar graph** visualization
* Result message page: congratulation if eligible, otherwise improvement suggestions 

 

## User Flow (High Level)

1. Open app (Flask web app)
2. Register / Login
3. Upload resume (docx)
4. Select company checkbox(es)
5. Submit → processing + scoring
6. View bar graph + message page

 

## Tech Stack

* **Backend**: Python
* **Web Framework**: Flask 
* **NLP**: NLTK (tokenization, stopwords, n-grams) 
* **Visualization**: Matplotlib (bar graph) 
* **Frontend**: HTML, CSS 
* **Database**: MySQL (MySQL Workbench used for setup) 
* **Resume Text Extraction**: docx2txt (docx → text) 

 

## System Architecture (Summary)

* **Client (Browser UI)**: Welcome / Login / Register / Upload pages
* **Flask Server**: Handles routing, file upload, processing pipeline
* **NLP Pipeline**: Extract → tokenize → clean → n-grams → match
* **MySQL DB**: Stores user login data
* **Output**: bar-graph visualization + eligibility message 

 

## Modules

As documented in the implementation section: 

1. **Frontend designs**

   * Welcome page
   * Login page
   * Register page
   * Upload page
2. **Backend Python**

   * Data extraction
   * Cleaning and preprocessing
   * Percentage calculation
3. **Visualization through Bar Graph**
4. **Message page**

 

## Setup and Installation

### Prerequisites

* Windows 7+
* Python installed
* MySQL Server + MySQL Workbench
* Basic Python packages for Flask + NLP + plotting 

### Database Setup (MySQL)

1. Create DB: `login`
2. Create table: `logininfo` with fields like `id`, `email`, `name`, `password` (as described) 

### Python Environment (Typical)

1. Create and activate a virtual environment
2. Install required packages (example):

   * flask
   * flask_mysqldb / MySQLdb
   * nltk
   * numpy
   * matplotlib
   * docx2txt

 

## How to Run

1. Clone the repository

   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. Install dependencies
3. Start the Flask app

   ```bash
   python app.py
   ```
4. Open in browser

   * Visit `http://localhost:5000` (the report references localhost usage for the UI) 

 

## Testing

Testing approaches covered in the report: 

* Black-box testing
* White-box testing
* Grey-box testing

Testing levels:

* Unit testing
* Integration testing
* System testing
* User acceptance testing 

Example validations included:

* Prevent register with an already-used email
* Wrong login credential handling
* Upload validation (docx + checkbox selection) 

 
## Future Enhancements

* Stronger authentication/security (avoid storing plain passwords)
* Better company requirement dataset management (admin panel / dynamic updates)
* Improved NLP matching (synonyms, embeddings, semantic similarity)
* Resume format support beyond docx (PDF parsing with robust extraction)
* Personalized improvement recommendations per missing skills/sections


## Contributors

**Batch B05 (Mini Project-I)** 

* Kollapudi Bindu Sri Nagavalli
* Komatlapalli Venkata Naga Sri
* Supraja Naraharisetty
* Mucherla Sai Sri Lakshmi Chaitanya
* Mancheela Neeraja Rajeshwari

 
```md
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

````

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

```
```

