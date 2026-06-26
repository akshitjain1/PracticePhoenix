# Production Operations & Reliability Manual

This document outlines the standard operational runbooks, diagnostic verification procedures, monitoring checks, database backup policies, and disaster recovery protocols for the Daily AI Preparation Platform.

---

## 1. Startup Diagnostics & Fail-Fast Verification

During application startup (`python -m app.main`), the platform automatically executes `StartupDiagnosticsService`. This service verifies:
- **Environment Configuration**: Asserts `TELEGRAM_BOT_TOKEN` and `GROQ_API_KEY` are present and valid.
- **Database Connectivity**: Executes a heartbeat query (`SELECT 1`) against SQLite.
- **Curriculum Assets**: Verifies JSON lesson files in `app/curriculum/assets/` can be parsed.
- **Export Permissions**: Tests file creation and deletion inside `data/exports/`.

If any diagnostic fails, the application prints a critical report and raises `RuntimeError`, terminating immediately. **The application never runs in a partial or degraded state.**

---

## 2. Live Health Monitoring (`/health`)

Administrators and users can inspect live subsystem health at any time via the `/health` Telegram command.

```json
{
  "status": "HEALTHY",
  "database": "UP",
  "ai_provider": "UP",
  "scheduler": "UP",
  "curriculum": "UP",
  "history_archive": "UP"
}
```
- **HEALTHY**: All subsystems active and responding.
- **DEGRADED**: Secondary services (e.g., AI provider API rate limits) temporarily unreachable.
- **UNHEALTHY**: Core persistence or curriculum store inaccessible.

---

## 3. Automated SQLite Database Backups

The `BackupService` manages automated hot backups of the active SQLite database (`data/preparation.db`).
- **Filename Convention**: `backups/preparation_backup_YYYYMMDD_HHMMSS.db`
- **Retention Policy**: Automated pruning keeps **exactly the last 14 backups**. When a 15th backup is created, the oldest chronological archive is purged automatically.

---

## 4. Graceful Shutdown Protocol

When receiving termination signals (`SIGINT`, `SIGTERM`, or `Ctrl+C`), `TelegramBot` executes its shutdown handler:
1. **Scheduler Termination**: `SchedulerService.stop()` cancels pending cron triggers and waits for active morning broadcasts to finish.
2. **Database Pool Closure**: Active SQLAlchemy sessions are closed safely.
3. **Network Cleanup**: Telegram HTTP polling connections disconnect without orphan threads.

---

## 5. Scheduled Job Idempotency

To prevent duplicate Telegram morning briefs due to restarts or retries around `07:00 IST`:
- E.g., `JobRunner` queries `HistoryRepository.exists_for_date(date.today())` before calling AI inference.
- If today's brief is already recorded, generation is skipped (`SKIPPED_DUPLICATE`) and zero duplicate messages are sent.
