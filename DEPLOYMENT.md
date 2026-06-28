# Production Deployment Guide

Follow these steps to deploy the production-hardened Daily AI Preparation Platform across Serverless GitHub Actions workflows, Docker containerized environments, Linux systemd daemons, or Windows NSSM background services.

---

## 1. Serverless GitHub Actions Deployment (Recommended Cloud Edition)

The platform supports zero-server, zero-polling serverless execution via scheduled GitHub Actions workflows (`.github/workflows/daily_brief.yml`). This eliminates the need for 24/7 cloud hosting while guaranteeing exact 07:00 IST morning deliveries backed by automated message chunking (`<4000` chars) and structured JSON fallback resilience.

### Setup Protocol
1. Fork or push this repository to GitHub.
2. Go to **Repository Settings** > **Secrets and variables** > **Actions**.
3. Add the following repository secrets:
   - `TELEGRAM_BOT_TOKEN`: Secret API token obtained from @BotFather
   - `GROQ_API_KEY`: Fast cloud LLM inference gateway key
   - `BROADCAST_CHAT_ID`: Target Telegram Chat ID or Channel ID for automated briefs
4. The workflow runs automatically every day at `00:30 UTC` (`06:00 IST`). You can also manually trigger generation anytime via **Actions** > **Scheduled Daily Brief Delivery** > **Run workflow**.

---

## 2. Containerized Docker Deployment (Local Interactive Edition)

For interactive bot commands (`/grill-me`, `/daily`, `/history`, `/search`), run the platform locally or on a VPS using Docker Compose.

### Execution Protocol
```bash
git clone https://github.com/akshit/daily-ai-preparation-bot.git
cd daily-ai-preparation-bot

cp .env.example .env
# Edit .env with your TELEGRAM_BOT_TOKEN, GROQ_API_KEY, and BROADCAST_CHAT_ID

docker compose up -d --build
```

---

## 3. Linux Server Deployment (Systemd Daemon)

For bare-metal Linux servers, configure a systemd background service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now daily-prep-bot.service
```

---

## 4. Windows Server Deployment (NSSM Service)

For Windows VPS environments, manage background execution via NSSM:
```powershell
nssm install DailyPrepBot "C:\deploy\daily-ai-preparation-bot\.venv\Scripts\python.exe" "-m app.main"
nssm start DailyPrepBot
```
