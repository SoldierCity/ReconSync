# ReconSync System Architecture

## 1. Overview

ReconSync is a modular, Discord-integrated bot-agent system designed for monitoring, alerting, and backing up game servers such as ARK, Rust, and Valheim. It allows admins to run slash commands via Discord, while lightweight Recon Agents perform server-side operations like scheduled backups and crash monitoring. Built for scalability and automation, ReconSync supports distributed operation across multiple servers.

---

## 2. Core Components

### Discord Bot

- **Language**: Python (discord.py)
- **Responsibilities**:
  - Handle slash commands (e.g. `/status`, `/backup now`)
  - Dispatch actions to appropriate agents
  - Publish alerts to Discord via webhooks or bot messages
  - Enforce permission roles (`User`, `Admin`, `Owner`)

### Recon Agent

- **Language**: Python (initial MVP)
- **Responsibilities**:
  - Load game-specific `config.yaml`
  - Perform local backups (e.g. zip game folders)
  - Monitor for crashes, abnormal behavior and health
  - Send telemetry and events: heartbeat, backup results, crash alerts
  - Deployed on game servers (Rust, ARK, Valheim, etc.)

### Command API Layer (Future)

- **Status**: Communication model still under evaluation
- **Candidates**: REST, WebSocket, Message Queue (RabbitMQ, RedisMQ)
- **Purpose**:
  - Allow structured, decoupled communication
  - Improve reliability and extensibility
 
### Config Schema

- **Format**: YAML (per game server)
- **Key Elements**:
  - `backup`: path, schedule, retention\_days
  - `monitor`: check\_interval, crash\_threshold
  - `server_id`, `game`, `map`
- See [game-profiles.md](game-profiles.md) for full format

### Scheduling System

- **Format**: Structured cron expression in config
- **Behavior**:
  - Schedule-based backup triggering
  - Timezone-aware via `timezone` field
  - Graceful fallback if config is malformed or unavailable

### Tech Stack

The implementation stack used across all core components is defined in [tech_stack.md](tech_stack.md). It includes:

- Python 3.11+ as the shared language for both bot and agent
- `discord.py`, `FastAPI`, `httpx`, `PyYAML`, and `APScheduler`
- Deployment via Docker or systemd
- Security and future extensibility considerations (e.g., JWT, WebSocket)

Refer to the full [tech stack and deployment model](tech_stack.md) for rationale and future plans.

---

## 3. Communication Protocol

- **Current Status**: TBD; see [decision-log.md](decision-log.md)
- **Authentication**: Pre-shared tokens or signed JWTs
- **Message Types**:
- `heartbeat`, `backup_result`, `crash_alert`, etc.
- **Reliability Plan**:
- Phase 2: basic HTTP dispatch
- Phase 3+: fallback queueing via RedisMQ or RabbitMQ

---

## 4. Discord Integration

- **Commands**:
  - `/status` — View server health
  - `/backup now` — Trigger manual backup
  - `/reboot` — Restart server (planned)
- **Permission Tiers**:
  - User: view-only
  - Admin: can invoke actions
  - Owner: full control
- **Command Lifecycle**:
  - Bot receives command ➔ dispatches to agent ➔ agent executes ➔ result returned to Discord
- **Notifications**:
  - Sent to specified channels via bot or webhook

---

## 5. Deployment Topology Diagram

```
[Discord UI]
    |
[ReconSync Bot]
    | Slash Cmds / Alerts
    v
[Command Dispatcher]
    |
    v
[Recon Agent(s)]  <-- Local config.yaml, backup path access
    |
    v
[Game Server: ARK, Rust, etc.]
```

- **Backup Folder Access**: `/home/container/serverdata` (example)
- **Config Path**: `config.yaml` loaded at agent startup
- **Alerts**: Discord Webhook or bot message to alert channel

---

## 6. Security Model

- **Discord OAuth2**: Used for bot integration and role mapping
- **Permissions**: Enforced via Discord roles (see [commands.md](commands.md)
- **Agent Auth**: Pre-shared key or JWT per game server
- **Access Scope**: Limited to only the server assigned to that agent
- **Future**: Optional encryption of messages (AES or TLS tunnels)

---

## 7. Extensibility Considerations

- **Planned Features**:
  - `/restore` command for backup recovery
  - Cloud backup destinations (S3, Dropbox, B2)
  - Auto-registration for agents and config templates
- **Design Hooks**:
  - Pluggable game templates in `games/`
  - Add-on monitors (e.g. player join/death/crash)
  - Dynamic command registration per server or admin

---

## 8. Roadmap Alignment

- MVP aligns with **Phase 2** of `project-plan.md`
  - Implements `/status`, `/backup now`
  - Adds agent ping, backup, and monitor
  - Integrates permission tiers
- Phase 3+:
  - Adds dynamic registration, restore, cloud sync
  - Enhances reliability via message queues

--- 
