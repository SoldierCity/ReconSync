# ReconSync

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

---

## Supported Games

- ARK: Survival Ascended
- Rust
- Valheim *(experimental)*

> Additional games (e.g., 7DTD, Minecraft) are planned for Phase 7.

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
├── agent/ # Recon Agent running on game servers
│ ├── backup.py
│ ├── monitor.py
│ └── config.yaml # Per-server config
├── bot/ # Discord Bot
│ └── main.py
├── games/ # Game config templates
│ ├── ark.yaml
│ └── rust.yaml
├── docs/ # Public user & dev documentation
│ ├── user/
│ └── dev/
├── scripts/ # Optional install helpers
│ ├── install.sh
│ └── install.bat
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

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

You are free to use, modify, and host ReconSync yourself. Hosted ReconSync services with additional features may be offered commercially by [SoldierCity.io](https://soldiercity.io).

---

## Contributing

We're currently building out the core infrastructure. Contributions are welcome once the v0.1.0 release is stabilized.

---

## Community

- Website: https://soldiercity.io
- Discord: *coming soon*
- GitHub Issues: [Submit a bug or request a feature](https://github.com/SoldierCity/ReconSync/issues)
