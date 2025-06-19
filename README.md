# ReconSync

https://github.com/SoldierCity/ReconSync

**ReconSync** is a modular, Discord-integrated bot-agent system for backing up and monitoring dedicated game servers like ARK and Rust.

### Features
- Slash-command interface via Discord
- Agent-based server monitoring and alerting
- Scheduled and manual backups
- Game-specific YAML config profiles

### Supported Games
- ARK: Survival Ascended
- Rust

### Minimum Viable Product (MVP) Goals (Phase 2)
- `/status`, `/backup now` commands
- Basic server uptime and crash monitoring
- Discord alert messages

### Structure
- `agent/` – Runs on game servers (monitoring, backups)
- `bot/` – Discord bot interface
- `games/` – Game-specific YAML templates
- `docs/` – User and dev docs
