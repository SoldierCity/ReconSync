# Design Decision Log

Track all major architectural decisions here.

---

### [2025-06-19] Repository Split for Design

**Decision**: Create a separate private repo for internal design documentation (`ReconSync-Internal`).

**Rationale**: Clean separation of implementation and high-level design. Prevents cluttering the public repo and encourages internal-only discussions.

---

### [2025-06-19] Slash Command Interface via Discord

**Decision**: Use Discord slash commands as the main interface for users.

**Rationale**: User-friendly, permission-mapped, and requires no external UI.

---

### [2025-06-19] Game Profile Format

**Decision**: Use YAML for game-specific config profiles.

**Rationale**: Human-readable, versionable, and widely supported in Python tooling.

---

### [2025-06-19] Move from Cron Strings to Structured Scheduling Format

**Decision**: Replace single-line cron strings in game profile config with structured schedule objects.

**Rationale**: Improves readability, validation, and future extensibility (e.g. support for different schedule types, timezones, GUI tools).

**Example**:
```yaml
schedule:
  type: cron
  expression: "0 * * * *"
  timezone: "UTC"
```

---

### [2025-06-19] Communication Protocol Between Bot and Agent

**Decision**: Use REST API for MVP (Phase 2) communication between bot and agent.

**Rationale**: HTTP is simple, stateless, easy to debug, and suitable for basic commands. Future versions (Phase 3+) may upgrade to WebSocket or MQ for better reliability and bi-directional messaging.

**Protocol Spec**: See `docs/bot-agent-protocol.md`

---

### [2025-06-19] Tech Stack & Deployment Model Selected

**Decision**:
- Language: Python
- Bot: `discord.py`, `httpx`
- Agent: `FastAPI`, `PyYAML`, `APScheduler`, `pydantic`
- Config: YAML
- Deployment: Bot via Docker or systemd; Agent via zip/installer or Docker
- Auth: Pre-shared token via `Authorization: Bearer`
- REST API for MVP; future: WebSocket or MQ
- Security: TLS, scoped tokens, optional signed payloads

**Rationale**: Aligns with MVP goals (simple, cross-platform), supports future extensibility (web dashboard, cloud sync), and is lightweight for game server environments.

### [2025-06-19] License Changed to Apache 2.0 for SaaS Readiness

**Decision**: Use the Apache License 2.0 for the public ReconSync GitHub repository.

**Rationale**: Apache 2.0 is a permissive open-source license with explicit patent protection. This choice aligns with plans to offer hosted (SaaS) versions of ReconSync in the future. It provides more legal clarity for contributors and better safeguards for commercial extensions.

**SaaS Scope** (planned in Phase 5–6):
- Hosted bot + agent management
- Discord-based and/or web UI control
- Optional cloud backup storage
- Freemium or subscription-based tiers
