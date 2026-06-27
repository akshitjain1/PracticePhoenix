# Changelog

All meaningful changes to this project will be documented in this file.

## [1.1.0] - Sprint 14 (Serverless GitHub Actions Deployment Architecture)

### Added
- Created standalone serverless root entrypoint (`run_daily.py`) handling database initialization, fail-fast diagnostics, date-based duplicate checking, daily brief synthesis, SQLite history archiving, and clean termination (`exit code 0`) without background loops.
- Created `app/utils/telegram_sender.py` (`TelegramSender`) encapsulating asynchronous Telegram API delivery, exponential Tenacity backoff retries, and plain text fallback upon Markdown parsing exceptions.
- Created scheduled GitHub Actions workflow (`.github/workflows/daily_brief.yml`) triggering morning delivery at `00:30 UTC` (`06:00 IST`) with repository secrets injection (`TELEGRAM_BOT_TOKEN`, `GROQ_API_KEY`, `BROADCAST_CHAT_ID`).
- Created unit tests (`tests/test_run_daily.py`) verifying mock dispatcher execution and serverless workflow status codes.
- Updated `test_revision_engine.py` to clean temporary revision queue tables before testing, ensuring dynamic date hygiene across full regression test suites.
- Updated `README.md`, `DEPLOYMENT.md`, `PROJECT_STATE.md`, and `CHANGELOG.md` documenting serverless cloud setup runbooks.
- Certified 100% green pass rate across 25 unit tests (`pytest`).

---

## [1.0.0] - Sprint 13 (Release Candidate Validation & General Availability)

### Added
- Created `RELEASE_NOTES_v1.0.0.md`, `PERFORMANCE.md`, `TROUBLESHOOTING.md`, `.dockerignore`, and RC resilience tests.

---

## [0.9.0] - Sprint 12 (Production Deployment Engineering Subsystem)

### Added
- Containerized Docker setup, CI automation, and host runbooks.
