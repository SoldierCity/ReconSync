# ReconSync Tech Stack & Deployment Model

_Last updated: 2025-06-19_

This document defines the technology choices and deployment strategy for the **ReconSync** project, which provides a modular, Discord-integrated system for monitoring and backing up game servers like ARK, Rust, and Valheim.

---

## 1. Core Tech Stack (MVP)

### Language & Runtime
- **Python 3.11+** — Chosen for cross-platform compatibility, mature ecosystem, and ease of integration with Discord and REST APIs.

### Libraries & Frameworks

| Function               | Library               | Notes |
|------------------------|-----------------------|-------|
| Discord Integration    | `discord.py`          | Handles slash commands, role permissions, and messaging |
| REST Client (Bot)      | `httpx`               | Async HTTP client used to contact agents |
| REST API (Agent)       | `FastAPI`             | Async, typed, OpenAPI-ready microservice framework |
| Config Parsing         | `PyYAML`              | Reads game profile `config.yaml` |
| Validation             | `pydantic`            | Validates config structure and message payloads |
| Scheduling             | `APScheduler`         | Supports cron-like jobs and async tasks |
| Logging                | `loguru` or `logging` | Structured, colorized logging with rotation and levels |

---

## 2. Deployment Model

### Bot Deployment
- **Method**: Docker container or `systemd` service
- **Runtime**: `venv` with `requirements.txt` or pre-built image
- **Startup**: `python3 bot/main.py`
- **Logging**: File logging and optional Discord alerting

### Agent Deployment
- **Method**: ZIP bundle for MVP (or Docker)
- **Hosting**: Linux or Windows game servers via `systemd`, `Task Scheduler`, or `Docker`
- **Startup**: `python3 agent/serve.py`
- **Config**: Requires `config.yaml` per server, located in `/agent/`
- **Auth**: Pre-shared token in config, passed via `Authorization: Bearer`

### Secret Management
- Tokens stored in `config.yaml`, never committed to source control
- `.env` override support planned in Phase 3+
- Systemd `EnvironmentFile` or Docker secrets in production environments

---

## 3. Future-Proofing

### Protocol Upgrade Paths
- **WebSocket (Phase 3+)**: For persistent connection and real-time streaming
- **Message Queue (Phase 4+)**: RabbitMQ or RedisMQ for retries, reliability, and async dispatch

### Cloud Integration
- AWS S3 via `boto3` or cloud-agnostic `rclone`
- Supports `cloud_target: s3` in config
- Planned UI/Dashboard integration for config management and agent status

### Extensibility
- Modular game support via `games/*.yaml`
- Dynamic slash commands (Phase 6+)
- Plugin-ready agent system
- REST endpoints can be exposed to external dashboards or management APIs

---

## 4. Packaging & Distribution

| Component | Format        | Details |
|-----------|---------------|---------|
| Bot       | Docker or pip | For self-hosted or containerized installs |
| Agent     | ZIP/tarball   | Simple install, cross-platform |
| Scripts   | `install.sh`, `install.bat` | Planned for Phase 3 |

### Config Placement
- `config.yaml` must be placed at `/agent/config.yaml`
- Strict schema validation enforced at startup
- Config updates require agent restart (live reload planned Phase 6)

---

## 5. Security Guidelines

### All agent communications use: Authorization: Bearer <token>
- TLS required in production (via Nginx reverse proxy or native HTTPS)
- Tokens should be long, random, and stored securely
- Optional future enhancements:
- IP whitelisting
- JWTs with expiration/issuer verification
- Signed payloads (HMAC/RSA)
- Rate limiting

---

## 6. Related Docs

- [architecture.md](architecture.md)
- [bot-agent-protocol.md](bot-agent-protocol.md)
- [game-profiles.md](game-profiles.md)
- [decision-log.md](decision-log.md)
