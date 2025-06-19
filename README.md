# ReconSync
[![License](https://img.shields.io/github/license/SoldierCity/ReconSync)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
> **Built With**: `discord.py`, `FastAPI`, `httpx`, `PyYAML`, `pydantic`, `APScheduler`

https://github.com/SoldierCity/ReconSync

**ReconSync** is a modular, Discord-integrated bot-agent system for backing up and monitoring dedicated game servers like  **ARK: Survival Ascended**, **Rust**, and **Valheim**.

It enables server admins to manage scheduled backups, monitor server health, and receive Discord alerts — all through simple slash commands.

---

### Minimum Viable Product (MVP) Features
- ✅ Slash-command interface via Discord:
  - `/status`, `/backup now`, `/uptime`, `/alerts enable`
- ✅ Agent-based monitoring and backups
- ✅ Cron-based scheduling and retention config
- ✅ Server health alerts in Discord
- ✅ YAML-based per-server config files
- ✅ Supports Linux & Windows game servers
> Built using [discord.py](https://discordpy.readthedocs.io/), [FastAPI](https://fastapi.tiangolo.com/), and [PyYAML](https://pyyaml.org/)

---

## Supported Games

- ARK: Survival Ascended
- Rust
- Valheim *(experimental)*

> Additional games (e.g., 7DTD, Minecraft) are planned for Phase 7.

---

## 🔧 Getting Started

To self-host ReconSync, clone this repo and configure your environment using the templates in `.env.example` and `games/*.yaml`.

> Full setup instructions coming soon in [`docs/user/`](docs/user/)

---

## Architecture Overview

- **Discord Bot**: Handles slash commands and permissions
- **Recon Agent**: Runs on each game server; performs backups and sends alerts
- **YAML Config**: Game-specific configuration (backup schedule, monitor rules)
- **REST Protocol**: Bot-Agent communication using secure tokens

---

## Project Structure
```bash
ReconSync/
├── agent/                  # Recon Agent running on game servers
│   ├── backup.py
│   ├── monitor.py
│   └── config.yaml         # Per-server config
├── bot/                    # Discord Bot
│   └── main.py
├── games/                  # Game config templates
│   ├── ark.yaml
│   └── rust.yaml
├── docs/                   # Public user & dev documentation
│   ├── user/
│   └── dev/
├── scripts/                # Optional install helpers
│   ├── install.sh
│   └── install.bat
├── .gitignore
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Roadmap Highlights

Planned features (post-MVP):
- `/restore` from previous backup
- Cloud backup targets (S3, Dropbox)
- Web dashboard & hosted UI
- JWT-based authentication
- Agent auto-registration

---

## Hosted (SaaS) Offering

ReconSync will offer a managed, hosted version for those who don’t want to self-host:

- Hosted Discord bot
- Cloud storage and retention
- Dashboard with monitoring and control
- Free tier + premium plans

> Join the [early access waitlist](https://soldiercity.io/reconsync) *(coming soon)*

---

## Testing

Automated test coverage and config validation are planned for Phase 3. For now, game profiles are manually verified.

---

## Contributing

ReconSync is under active development. If you're interested in contributing before v0.1.0 is finalized, feel free to open issues or contact us via GitHub Discussions.

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

You are free to use, modify, and self-host ReconSync under the terms of the Apache 2.0 License. Hosted ReconSync services with additional features may be offered commercially by [SoldierCity.io](https://soldiercity.io).

---

## Community

- Website: https://soldiercity.io
- Discord: *coming soon*
- GitHub Issues: [Submit a bug or request a feature](https://github.com/SoldierCity/ReconSync/issues)
