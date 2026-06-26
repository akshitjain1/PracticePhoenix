# Troubleshooting & Diagnostic Matrix

Use this operational runbook to diagnose and resolve deployment exceptions, network timeouts, API rate limits, and scheduling misfires.

---

## 1. Telegram Polling Conflicts (`Conflict: terminated by other getUpdates`)

### Symptom
Container logs show repeated `telegram.error.Conflict: terminated by other getUpdates request; make sure that only one bot instance is running`.

### Root Cause
Multiple background container instances or local development scripts are attempting to poll Telegram servers using the same `TELEGRAM_BOT_TOKEN`.

### Resolution
1. List all active Docker containers: `docker ps`
2. Stop duplicate containers: `docker stop <container_id>`
3. Ensure local scripts (`python -m app.main`) are terminated before starting Docker Compose.

---

## 2. Groq Cloud Inference Gateway Errors (`HTTP 429 Too Many Requests`)

### Symptom
LLM generation fails or retries with `groq.APIStatusError: Error code: 429`.

### Root Cause
Free-tier or tier-1 token per minute (TPM) limits exceeded during wave-parallel generation.

### Resolution
- Built-in Tenacity retry decorators automatically wait and re-execute requests up to 3 attempts.
- If persistent, upgrade your Groq API tier or switch model profiles to budget/gemini fallback.

---

## 3. SQLite Database Locking (`sqlite3.OperationalError: database is locked`)

### Symptom
Background telemetry logging or scheduled brief writes raise database locked warnings.

### Root Cause
Long-running synchronous transactions blocking thread-safe SQLite write locks.

### Resolution
- The platform uses short-lived SQLAlchemy context managers (`with SessionLocal() as session:`). Ensure no manual database GUI tools (e.g. DB Browser) are keeping open write locks on `data/preparation.db`.

---

## 4. Morning Scheduler Misfires (Brief Not Sent at 07:00)

### Symptom
No daily brief arrives in Telegram at 07:00 IST.

### Resolution
1. Verify host timezone setting in `.env` (`TIMEZONE=Asia/Kolkata`).
2. Inspect health diagnostics via `/health` Telegram command.
3. Check `JobRunner` logs for `SKIPPED_DUPLICATE` (indicates brief was already generated during an earlier restart today).
