# Daily AI Preparation Platform (GA v1.2.0 / Stable Serverless Edition)

A production-stabilized, containerized, and serverless automated daily preparation platform designed to deliver structured software engineering interview briefs, spaced repetitions, comprehensive study analytics, personalized mentoring advice, interaction telemetry, live diagnostic monitoring, automated hot SQLite backups, and adaptive Socratic interview practice (`/grill-me`) via Telegram.

## Overview

The Daily AI Preparation Platform curates interview topics across core computer science domains (Operating Systems, DBMS, Computer Networks), Backend Engineering, AI Engineering, and Data Structures & Algorithms. It leverages advanced LLM reasoning (via Groq/Gemini) with deterministic structured JSON output mode to generate comprehensive daily study briefs formatted cleanly for Telegram. Backed by an automated spaced repetition engine, intelligent message chunking (`<4000 chars`), isolated fallback resilience, interaction telemetry, fail-fast diagnostics, scheduled GitHub Actions workflows, Docker containerization, and interactive Socratic interview practice.

## Key Production Stabilization (v1.2.0) Features

- **Intelligent Telegram Message Chunking**: Automated `MessageChunker` splitting large formatted preparation briefs (`>4000` chars) along logical Markdown section boundaries, guaranteeing sequential delivery and eliminating Telegram 4096 character limits.
- **Strict Structured JSON Mode**: Native `response_format={"type": "json_object"}` API integration combined with explicit prompt constraints preventing nested markdown dicts and parsing failures.
- **Isolated Section Resilience**: Wave-parallel generator execution wrapped in fail-safe fallback containers ensuring single section timeouts (e.g. AI Engineering) never impact surrounding domains.
- **Serverless Checkmark Telemetry**: Clean structured diagnostic logging auditing the exact generation lifecycle (`✓ Startup diagnostics`, `✓ Curriculum loaded`, `✓ Chunk 1 delivered`, `✓ Daily brief completed`).
- **Serverless Cloud Delivery**: Scheduled GitHub Actions workflow (`.github/workflows/daily_brief.yml`) running a standalone execution script (`run_daily.py`). Delivers daily preparation briefs at exact morning intervals without requiring 24/7 server polling or background scheduler daemons.
- **Preserved Local Interactive Bot**: Full interactive Telegram polling application (`python -m app.main`) preserved for local debugging, Socratic interviews (`/grill-me`), knowledge searches (`/search`), and live system monitoring (`/health`).

## Available Telegram Commands (Local Interactive Edition)

### System Health & Diagnostics
- `/health` - Inspect live diagnostic status across database, AI gateway, scheduler, and repositories
- `/test` - Verify active bot connection heartbeat

### Study & Scheduling
- `/start` - Initialize bot connection and welcome guide
- `/help` - Show available commands and usage guide
- `/daily` - Manually trigger generation and delivery of today's study brief

### Interactive AI Interview Practice
- `/grill-me [category]` - Launch an adaptive AI interview practice session on your weakest or selected domain
- `/stop-grill` - Conclude active interview practice session and view summary report
- `/score` - Check live average evaluation performance during active practice
- `/hint` - Receive conceptual engineering hint for active practice question
- `/skip` - Advance to next interview practice question

### Knowledge Management & Analytics
- `/history` - View recent daily study briefs recorded in your archive
- `/search <keyword>` - Search through past preparation briefs by keyword
- `/topic <topic>` - Retrieve the latest comprehensive study lesson covering a specific topic
- `/export` - Export and download your complete historical study record as a Markdown document
- `/progress` - Curriculum completion overview and track percentages
- `/stats` - Platform analytics, study volume, and streak statistics
- `/streak` - Consecutive daily study streak motivation report
- `/weaknesses` - Ranked domain weaknesses based on review queue load
- `/roadmap` - Estimated remaining lesson roadmap timeline

## Official Release Documentation Runbooks
- [Production Deployment Guide](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/DEPLOYMENT.md) (Serverless GitHub Actions, Docker, systemd, NSSM)
- [GA v1.0.0 Release Notes](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/RELEASE_NOTES_v1.0.0.md)
- [Performance Benchmarks](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/PERFORMANCE.md)
- [Troubleshooting Matrix](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/TROUBLESHOOTING.md)
