LIVE AT - https://internhub-ai-agent.onrender.com/

# InternHub AI Agent

**TL;DR**  
A minimal LLM powered AI agent that evaluates internship fit using structured prompt engineering.  
Built with **Groq** and focused on **explainable reasoning over UI**.

---

## Overview

An LLM powered AI agent that evaluates how well a student profile matches an internship role using structured prompt engineering and Groq LLM.

Built as part of the **AI Engineering Intern assignment for Kadeep Technologies**.

Students often struggle to judge whether they are a good fit for an internship. They either apply blindly or miss opportunities they could realistically crack with small improvements.

This project addresses that problem by building a lightweight AI agent that:

- Analyzes a student profile against an internship description  
- Explains the level of fit in a clear and structured way  
- Highlights skill gaps and improvement areas  
- Generates resume-ready insights  

The focus of this project is **LLM reasoning, prompt design, and explainable outputs**, not UI or complex infrastructure.

---

## What the Agent Does

Given a student profile and an internship job description, the agent generates:

### Match Percentage
A score from **0 to 100** indicating overall fit.

### Skill Gap Analysis
- Matching skills  
- Missing skills  
- Nice-to-have skills  

### Recommendation
A short, honest assessment on whether the student should apply.

### Tailored Resume Summary
A concise, ATS friendly professional summary aligned with the job description.

### ATS / Confidence Score
A score with reasoning indicating screening readiness.  

---

## Tech Stack

| Area | Technology |
|  --- |    ---     |
| Language | Python 3.8+ |
| Backend | Flask |
| Frontend | HTML + CSS (minimal, vanilla) |
| LLM | Groq API (LLaMA 3.1 8B) |
| Deployment | Render (free tier) |

---

# How It Works
# High Level Flow
User Input (Web UI or CLI)
↓
AI Agent Logic (agent.py)
↓
Five Task Specific Prompts
↓
Groq LLM API
↓
Structured, Explainable Output

---

## Prompt Engineering Approach

Instead of using one large prompt, the agent uses **five independent prompts**, each responsible for one task:

- Match analysis  
- Skill gap identification  
- Recommendation reasoning  
- Resume summary generation  
- ATS / confidence scoring  

This approach was chosen because it is:

- Easier to debug  
- Easier to improve incrementally  
- More explainable  
- Closer to real-world AI agent design  

Each prompt is:
- Task focused  
- Context rich  
- Explicit about output format  
- Designed for consistent responses  

---

## Project Structure

internhub-ai-agent/
├── main.py # CLI interface

├── app.py # Flask web app

├── agent.py # Core AI agent logic

├── config.py # API configuration

├── requirements.txt # Dependencies

├── .env # API key (git ignored)

├── .gitignore

├── templates/
│ └── index.html # Minimal web UI

├── example_inputs/
│ ├── student_profile.json
│ └── internship_jd.json

└── README.md


---

## Installation

### 1. Get Groq API Key (Free)

- Visit: https://console.groq.com/keys  
- Create an API key  
- Copy the key (starts with `gsk_`)

### 2. Clone and Setup

```bash
git clone https://github.com/Shreshth-Ghub/internhub-ai-agent.git
cd internhub-ai-agent

python -m venv venv


Windows-
venv\\Scripts\\activate

macOS / Linux
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

3. Configure Environment
Create a .env file:
GROQ_API_KEY=your_api_key_here

Usage
Option 1: CLI (Predefined Example)
python main.py

Option 2: CLI (Interactive)
python main.py

Option 3: Web Interface (Local)
python app.py

Open http://localhost:5000 in your browser.

## Example Output (Condensed)

The agent produces a clear and easy-to-understand evaluation of internship fit.  
For example, a typical output may indicate a **match score of 82%**, highlighting that the candidate has strong alignment with the role. It identifies **vector databases and RAG systems** as skill gaps and provides a concise recommendation stating that the candidate is a strong fit overall, with specific guidance on what to improve to further strengthen their profile.

---

## Design Decisions

### Why Minimal UI

The user interface is intentionally minimal and acts only as a thin interaction layer for the AI agent. The goal of this project was not to build a visually rich frontend, but to focus on the core AI engineering aspects such as LLM reasoning, prompt design, and explainable outputs. This approach aligns directly with Kadeep AI’s emphasis on building practical AI agents and automation workflows rather than frontend heavy applications.

---

## Assumptions

This project assumes that the student profile provided accurately reflects the candidate’s skills and experience, and that the internship description includes the key requirements and responsibilities of the role. The system expects English language input and requires an active internet connection to access the Groq LLM API. No persistent storage is used, as results are generated and displayed in real time.

---

## Future Improvements

With additional time, this project could be extended by introducing embedding based semantic matching to improve accuracy, integrating RAG pipelines with vector databases, and generating complete resume PDFs instead of summaries. Other potential improvements include caching responses, adding rate limiting, and incorporating a feedback loop to continuously improve recommendation quality.

```

Candidate Information

Name: Shreshth Gupt
Enrollment: E22CSEU0661
Batch: 2022
University: Bennett University
Location: Faridabad, Haryana
Role Applied For: AI Engineering Intern – Kadeep Technologies


Phone: 9599208146

Email: e22cseu0661@bennett.edu.in

GitHub: https://github.com/Shreshth-Ghub

LinkedIn: https://www.linkedin.com/in/shreshthgupt/
