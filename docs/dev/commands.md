# ReconSync Discord Bot Slash Command Reference

This document defines the complete slash command interface for **ReconSync**, a Discord-integrated bot-agent system used for backing up and monitoring game servers like ARK, Rust, and Valheim.

All commands are executed via Discord using **slash commands** (e.g., `/status`) and routed to server-side **Recon Agents**, which perform tasks like monitoring, backups, and restores. Command execution is scoped to a target `server_id`, matching the configuration profiles defined in [`game-profiles.md`](game-profiles.md).

Access is gated by Discord roles — `User`, `Admin`, and `Owner` — enforced by the bot before any action is dispatched.

---

## 📖 Command Reference

| Command             | Description                                 | Arguments                                | Permission |
|---------------------|---------------------------------------------|------------------------------------------|------------|
| `/status`           | Get server health and agent status          | `server_id`                              | User       |
| `/uptime`           | View server uptime and crash history        | `server_id`                              | User       |
| `/backup now`       | Trigger immediate server backup             | `server_id`                              | Admin      |
| `/reboot`           | Reboot the game server                      | `server_id`, `reason`                    | Admin      |
| `/config view`      | View the current loaded config              | `server_id`                              | Admin      |
| `/alerts enable`    | Enable in-Discord alerts (joins, deaths)    | `server_id`                              | Admin      |
| `/alerts disable`   | Disable in-Discord alerts                   | `server_id`                              | Admin      |
| `/agent register`   | Register new agent to bot and Discord link  | `server_id`, `auth_token`                | Owner      |
| `/restore`          | Restore a previous backup                   | `server_id`, `timestamp` or `latest`     | Owner      |

> ✅ *All commands support autocomplete for `server_id` where possible.*

---

## 🔐 Permission Roles

ReconSync relies on Discord roles to enforce proper access control. These roles are mapped internally and used by the bot to gate functionality.

| Role   | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| User   | Can run read-only and monitoring commands like `/status` and `/uptime`.     |
| Admin  | Can trigger actions like backups, reboots, and alert toggling.              |
| Owner  | Has full control, including agent registration and backup restore.          |

---

## ⚙️ Command Lifecycle

Each command follows the same lifecycle from invocation to execution:

1. **User triggers** a slash command in Discord (e.g., `/backup now server_id:ark-west`).
2. **Bot verifies** permissions and validates arguments.
3. **Bot dispatches** the command to the correct Recon Agent associated with that `server_id`.
4. **Agent executes** the operation (e.g., triggers a backup or reboots the game server).
5. **Result is returned** to Discord, shown in-channel or via a DM, and optionally logged or alerted.

---

## 🧩 Extensibility Notes

- Commands are designed to be **modular and extensible**, enabling future support for:
  - Game-specific commands (e.g., `/ark purge-logs`)
  - Dynamic command registration per server or agent
  - Cloud backup targets (`/backup to s3`)
  - Discord-based profile editing or YAML import
- Future versions (Phase 6+) will support **automatic command discovery** via agent registration.

See [architecture.md](architecture.md) and [roadmap.md](roadmap.md) for planned roadmap details.

---

## 📌 Notes

- All commands assume a valid game server profile exists for the `server_id` under `config.yaml`.
- See [`game-profiles.md`](game-profiles.md) for format and validation rules.
- Communication between bot and agent is evolving — see [`decision-log.md`](decision-log.md) for transport design updates
