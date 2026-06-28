# Changelog

All meaningful changes to this project will be documented in this file.

## [1.2.0] - Sprint 15 (Final Production Stabilization Subsystem)

### Added
- Created `app/utils/message_chunker.py` (`MessageChunker`) implementing intelligent splitting along logical Markdown section boundaries with a strict `4000` character limit.
- Refactored `TelegramSender` (`app/utils/telegram_sender.py`) to sequentially dispatch message chunks with isolated per-chunk retry backoffs and checkmark delivery telemetry (`✓ Chunk {i} delivered`).
- Enabled native API structured JSON output mode (`response_format={"type": "json_object"}`) in `GroqProvider` with seamless completion fallbacks.
- Updated all 8 prompt templates in `app/ai/prompts/` to enforce flat markdown string returns, eliminating schema validation mismatches caused by nested dictionaries.
- Wrapped wave-parallel generator executions in `DailyService` (`app/services/daily_service.py`) with guaranteed section fallbacks, ensuring isolated failures never crash daily brief assembly.
- Added structured checkmark telemetry (`✓ Startup diagnostics`, `✓ Curriculum loaded`, `✓ Revision queue loaded`, `✓ Formatter completed`, `✓ Daily brief completed`) across `run_daily.py` and `DailyService`.
- Created comprehensive unit test suite (`tests/test_message_chunker.py`) covering chunk boundary rules, markdown preservation, malformed JSON recovery, and section isolation.
- Certified 100% green pass rate across 30 unit tests (`pytest`).
- Updated `README.md`, `DEPLOYMENT.md`, `PROJECT_STATE.md`, and `CHANGELOG.md`.

---

## [1.1.0] - Sprint 14 (Serverless GitHub Actions Deployment Architecture)

### Added
- Created standalone serverless root entrypoint (`run_daily.py`) and scheduled CI workflow (`.github/workflows/daily_brief.yml`).

---

## [1.0.0] - Sprint 13 (Release Candidate Validation & General Availability)

### Added
- Created `RELEASE_NOTES_v1.0.0.md`, `PERFORMANCE.md`, `TROUBLESHOOTING.md`, `.dockerignore`, and RC resilience tests.
