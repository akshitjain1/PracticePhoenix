# Daily AI Preparation Platform (GA v1.0.0)

A containerized, production-grade automated daily preparation platform designed to deliver structured software engineering interview briefs, spaced repetitions, comprehensive study analytics, personalized mentoring advice, interaction telemetry, live diagnostic monitoring, automated hot SQLite backups, and adaptive Socratic interview practice (`/grill-me`) via Telegram.

## Overview

The Daily AI Preparation Platform curates interview topics across core computer science domains (Operating Systems, DBMS, Computer Networks), Backend Engineering, AI Engineering, and Data Structures & Algorithms. It leverages advanced LLM reasoning (via Groq/Gemini) to generate comprehensive daily study briefs formatted cleanly for Telegram, backed by an automated spaced repetition, analytics, career coaching, interaction telemetry, fail-fast diagnostics, Docker containerization, and interactive interview practice engine.

## Key General Availability (v1.0.0) Features

- **Official GA Release**: Verified steady-state performance baselines (`<500ms` startup, `~70MB` RAM), failure injection trapping, and clean `.dockerignore` context optimization.
- **Repeatable Docker Containerization**: Multi-stage/slim `Dockerfile` and `docker-compose.yml` supporting persistent volume mounts for SQLite databases (`/app/data`), backups (`/app/backups`), and logs (`/app/logs`).
- **Automated CI Validation**: Built-in GitHub Actions CI pipeline (`.github/workflows/ci.yml`) automatically executing dependency builds and 23 pytest unit tests on every push.
- **Fail-Fast Startup Validation**: Automated `StartupDiagnosticsService` verifying environment variables, SQLite connectivity, curriculum stores, and disk write permissions before starting.
- **Live Monitoring Endpoint**: `/health` command returning structured diagnostic health status across all active subsystems.
- **Scheduled Job Idempotency**: Built-in duplicate brief prevention ensuring 07:00 IST morning broadcasts never send duplicate messages.
- **Automated Hot Backups**: `BackupService` archiving SQLite databases with timestamped filenames and automated 14-backup retention cleanup.

## Available Telegram Commands

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
- [GA v1.0.0 Release Notes](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/RELEASE_NOTES_v1.0.0.md)
- [Production Deployment Guide](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/DEPLOYMENT.md)
- [Performance Benchmarks](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/PERFORMANCE.md)
- [Troubleshooting Matrix](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/TROUBLESHOOTING.md)
- [Production Operations Manual](file:///d:/Daily%20AI%20-powered%20Telegram%20bot/telegram-prep-bot/OPERATIONS.md)
