# Architectural Changelog – ReconSync

Track changes to architecture, design docs, and config formats here.

---

### [2025-06-19] Initial Design Repo Setup

- Created folder structure under `/docs`
- Added starter markdown files for architecture, decisions, commands, game_profiles, roadmap and changelog
- Drafted iniital architecture overview and sample game config
- Added `project-plan.md`, `architecture.md`, `commands.md`, and `game-profiles.md`
- Defined initial YAML game profile structure
- Outlined iniital MVP command set and game support

---

### [2025-06-19] Backup Schedule Format Overhaul

- Moved from cron strings to structured scheduling objects
- All `game_profiles` updated to support:
  ```yaml
  schedule:
    type: cron
    expression: "0 * * * *"
    timezone: "UTC"

---

### [2025-06-19] MVP Architecture Revamp

- Expanded `architecture.md` to fully reflect MVP scope from `project-plan.md`
- Defined core components: Discord Bot, Recon Agent, Config Schema, Scheduling System
- Added communication protocol evaluation (REST, WebSocket, MQ)
- Detailed command/response flow, Discord integration, permission tiers
- Included updated deployment topology diagram and security model
- Anticipated extensibility for restore, cloud sync, and modular game support
- Aligned with `commands.md`, `game-profiles.md`, and `decision-log.md`

---

### [2025-06-19] Slash Command Spec Finalized

- Rewrote `commands.md` to reflect production-ready spec
- Added intro, command reference table, lifecycle, and permission roles
- Aligned with `architecture.md`, `project-plan.md`, and `game-profiles.md`
- Structured for future extensibility and dynamic registration (Phase 6+)

---

### [2025-06-19] Bot-Agent Protocol Finalized

- Added `bot-agent-protocol.md` to define MVP communication between bot and agent
- Standardized message types: `heartbeat`, `status_response`, `backup_result`, `crash_alert`
- Defined HTTP request routing, authentication model, error handling, and extensibility

---

### [2025-06-19] Backup Scheduling Format Change

- Replaced cron strings with structured schedule objects
- Documented new format in `decision-log.md` and sample game profiles

---

