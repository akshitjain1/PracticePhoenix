# Production Deployment Guide

Follow these steps to deploy the production-hardened Daily AI Preparation Platform across Docker containerized environments, Linux systemd daemons, or Windows NSSM background services.

---

## 1. Containerized Docker Deployment (Recommended)

The platform includes a production-ready `Dockerfile` and `docker-compose.yml` configured for automatic volume mounting and timezone synchronization.

### Execution Protocol
```bash
# Clone repository and navigate to root
git clone https://github.com/akshit/daily-ai-preparation-bot.git
cd daily-ai-preparation-bot

# Configure credentials
cp .env.example .env
# Edit .env with your TELEGRAM_BOT_TOKEN, GROQ_API_KEY, and BROADCAST_CHAT_ID

# Build and start background container
docker compose up -d --build
```

### Storage Persistence Guarantee
The `docker-compose.yml` specification mounts local host folders into container volume mount points:
- `./data:/app/data` (SQLite database persistence)
- `./backups:/app/backups` (Hot database backup archives)
- `./logs:/app/logs` (Structured Loguru rotating log files)

---

## 2. Linux Server Deployment (Systemd Daemon)

For bare-metal or cloud Linux servers (Ubuntu/Debian/CentOS), configure a systemd background service.

### Service File Creation (`/etc/systemd/system/daily-prep-bot.service`)
```ini
[Unit]
Description=Daily AI Preparation Telegram Platform Daemon
After=network.target

[Service]
Type=simple
User=deploy
WorkingDirectory=/opt/daily-ai-preparation-bot
ExecStart=/opt/daily-ai-preparation-bot/.venv/bin/python -m app.main
Restart=always
RestartSec=5
EnvironmentFile=/opt/daily-ai-preparation-bot/.env

[Install]
WantedBy=multi-user.target
```

### Daemon Activation
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now daily-prep-bot.service
sudo systemctl status daily-prep-bot.service
```

---

## 3. Windows Server Deployment (NSSM Service)

For Windows VPS environments, manage background execution via NSSM (Non-Sucking Service Manager).

### NSSM Setup Commands
```powershell
nssm install DailyPrepBot "C:\deploy\daily-ai-preparation-bot\.venv\Scripts\python.exe" "-m app.main"
nssm set DailyPrepBot AppDirectory "C:\deploy\daily-ai-preparation-bot"
nssm set DailyPrepBot AppStdout "C:\deploy\daily-ai-preparation-bot\logs\service_output.log"
nssm set DailyPrepBot AppStderr "C:\deploy\daily-ai-preparation-bot\logs\service_error.log"
nssm start DailyPrepBot
```

---

## 4. Locked Dependency Maintenance Protocol

Platform dependencies are strictly locked inside `requirements.txt`.
- **Update Protocol**: To upgrade packages safely, test locally inside `.venv`, verify the 20 pytest unit tests pass, and commit the updated `requirements.txt` lockfile. CI automation will automatically re-verify build stability.
