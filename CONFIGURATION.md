# Configuration & Environment Reference

All platform settings are managed via environment variables loaded from `.env` or passed via container environments. Use `.env.example` as a baseline template.

## Required Environment Variables

| Variable | Type | Example | Description |
| :--- | :---: | :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | Secret String | `7123456789:AAH...` | Bot API token obtained from @BotFather |
| `GROQ_API_KEY` | Secret String | `gsk_ABC123...` | Cloud API key for fast LLM inference gateway |
| `BROADCAST_CHAT_ID` | String | `-100987654321` | Target Chat/Channel ID for automated 07:00 IST briefs |

## Optional Operational Settings

| Variable | Default | Description |
| :--- | :---: | :--- |
| `DATABASE_PATH` | `data/preparation.db` | Filesystem path to primary SQLite database |
| `SEND_TIME` | `07:00` | Local broadcast delivery schedule (24h HH:mm format) |
| `TIMEZONE` | `Asia/Kolkata` | Cron scheduler IANA timezone (`UTC`, `America/New_York`) |
| `LOG_LEVEL` | `INFO` | Rotating structured log verbosity (`DEBUG`, `INFO`, `ERROR`) |

## Dependency Locking Reference
Platform dependencies are pinned with exact versions in `requirements.txt`. Automated CI workflows (`.github/workflows/ci.yml`) enforce strict test validation against these exact package pins on every pull request.
