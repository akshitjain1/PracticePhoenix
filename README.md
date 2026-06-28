# PracticePhoenix 🚀

**PracticePhoenix** is an autonomous, serverless **AI Career Mentor** and daily technical preparation engine designed for ambitious software engineers preparing for FAANG+ tier systems design and coding interviews. Built with Python, FastAPI, SQLAlchemy, and Telegram, PracticePhoenix delivers compounding daily mentorship briefs directly to your Telegram client at `07:00 IST` or exposes clean JSON REST APIs for integration.

---

## Features & Philosophy

- 🤖 **Autonomous AI Mentorship**: Compounding daily curriculum covering Core CS, Backend Engineering, AI/LLM Engineering, DSA, System Design, Linux, and SQL.
- 📬 **Serverless Telegram Delivery**: Scheduled daily delivery powered by GitHub Actions serverless cron workflows with zero infrastructure maintenance.
- ⚡ **FastAPI REST Layer**: Exposes core preparation domain engines through typed JSON endpoints (`/health`, `/session/today`, `/revision`, `/progress`, `/history`, `/analytics`, `/roadmap`).
- 🧠 **Spaced Repetition & Recall**: Active recall loops and structured interview question banks designed to ensure long-term retention.

---

## Architecture Overview

```
app/
├── ai/                                     # LLM formatting, prompt templates & schema definitions
├── api/                                    # FastAPI REST API Layer & routes
├── models/                                 # SQLAlchemy ORM database models
└── services/                               # Core preparation domain engines & generators
curriculum/                                 # JSON curriculum topic assets & progression schedules
tests/                                      # Automated integration & unit test suite
```

---

## Running Locally

### 1. Environment Setup

Copy `.env.example` to `.env` and configure your API keys:

```bash
cp .env.example .env
```

### 2. Run API Server

Launch the local FastAPI server:

```bash
.venv\Scripts\uvicorn app.api.main:app --host 127.0.0.1 --port 8000 --reload
```

### 3. Trigger Daily Brief Execution

Manually generate and broadcast today's daily brief:

```bash
.venv\Scripts\python run_daily.py
```

---

## Testing & Verification

PracticePhoenix maintains a verified 100% green test suite (`pytest`) covering regression and API integration tests across HTTP endpoint contracts, message chunking, schema defaults, modular generator fallbacks, serverless execution flows, and reliable delivery mechanics.

```bash
# Run backend verified test suite
.venv\Scripts\pytest
```
