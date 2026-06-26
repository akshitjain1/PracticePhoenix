# Project Structure & Architectural Boundaries

This document defines the codebase layout and enforces architectural boundaries across the Daily AI Preparation Platform.

## Directory Layout

```text
telegram-prep-bot/
├── app/
│   ├── ai/                 # AI Generation & LLM Abstraction
│   │   ├── providers/      # LLM API communication implementations
│   │   ├── schemas/        # Pydantic validation schemas
│   │   ├── formatter.py    # Telegram Markdown presentation formatting
│   │   ├── generator.py    # Service-level AI generation facade
│   │   ├── prompt_builder.py # Curriculum prompt construction
│   │   └── response_parser.py # JSON response cleanup & schema validation
│   ├── bot/                # Telegram Bot Layer
│   │   ├── bot.py          # Bot initialization & handler registration
│   │   └── handlers.py     # Command receivers (/start, /help, /daily)
│   ├── config/             # Application Configuration
│   │   └── settings.py     # Environment variable loading (pydantic-settings)
│   ├── curriculum/         # Curriculum Definitions
│   │   └── tracks.py       # Topic lists across CS domains
│   ├── database/           # Database Engine & Migrations
│   │   ├── database.py     # SQLAlchemy engine & SessionLocal factory
│   │   ├── init_db.py      # Schema initialization utility
│   │   └── models.py       # DeclarativeBase foundation
│   ├── models/             # SQLAlchemy ORM Entities
│   │   ├── history.py      # Daily history records
│   │   ├── progress.py     # Curriculum tracking records
│   │   └── revision.py     # Spaced-repetition queue items
│   ├── repositories/       # Data Access Layer
│   │   └── progress_repository.py # Database queries for curriculum index
│   ├── scheduler/          # Cron & Background Job Automation
│   ├── services/           # Business Logic Layer
│   │   ├── curriculum_service.py # Topic rotation logic
│   │   └── daily_service.py      # Orchestrates brief generation workflow
│   ├── templates/          # Prompt & Message Templates
│   ├── utils/              # Shared Infrastructure & Utilities
│   │   └── logger.py       # Loguru logger configuration
│   └── main.py             # Canonical Application Entry Point
├── data/                   # SQLite Database File Storage
├── docs/                   # Architectural & Domain Documentation
├── logs/                   # Rotating Application Log Files
├── tests/                  # Pytest Unit & Integration Test Suite
│   └── test_daily_brief.py # Verified test suite
├── CHANGELOG.md            # Version History
├── CONFIGURATION.md        # Environment Settings Reference
├── DEPLOYMENT.md           # Production Deployment Guide
├── PROJECT_STATE.md        # Current Sprint & Status Report
├── PROJECT_STRUCTURE.md    # Codebase Layout Reference (This File)
├── README.md               # Overview & Quickstart Guide
├── pytest.ini              # Pytest Configuration
└── requirements.txt        # Pinned Python Dependencies
```

---

## Architectural Rules & Separation of Concerns

1. **Telegram Handlers (`app/bot/handlers.py`)**:
   - **Responsibility**: Receive incoming updates and return formatted responses.
   - **Restriction**: Must *never* contain business logic or directly communicate with database sessions or LLM APIs. Handlers delegate exclusively to Services.

2. **Services (`app/services/`)**:
   - **Responsibility**: Contain all core domain and business logic (e.g., orchestrating prompt generation, calling AI generators, completing curriculum steps).

3. **Repositories (`app/repositories/`)**:
   - **Responsibility**: Encapsulate all database queries and SQLAlchemy ORM mutations.
   - **Restriction**: Business logic and Telegram formatting must never leak into repositories.

4. **AI Providers (`app/ai/providers/`)**:
   - **Responsibility**: Communicate directly with external LLM APIs (Groq, Gemini, OpenAI).
   - **Restriction**: Providers only accept string prompts and return raw string outputs. Prompt building and response validation occur upstream.

5. **Prompt Builders & Formatters (`app/ai/`)**:
   - **Responsibility**: `PromptBuilder` transforms domain models into strict LLM instructions. `TelegramFormatter` transforms validated domain schemas into Markdown strings suitable for Telegram chat rendering.
