# Game Profile Configuration – `config.yaml`

Each game server running a **Recon Agent** must have its own YAML configuration file. This file controls backup scheduling, crash monitoring, and integration with the Discord bot. It is mandatory for every agent and must be loaded at startup.

- **Path**: `/agent/config.yaml`
- **Format**: YAML (strict schema, validated at agent load)
- **Scope**: One file per server instance

---

## Standard Schema Reference

Below is the full schema reference for a production-ready game profile:

```yaml
game: rust
server_id: rust-east-001
map: Procedural Map

cloud_target: s3
auto_update: false

env:
  DEBUG: true
  REGION: us-east-1

backup:
  path: /home/container/serverdata
  schedule:
    type: cron
    expression: "0 * * * *"
    timezone: "UTC"
  retention_days: 7
  cloud_target: s3
  auto_update: false
  env:
    DEBUG: true
monitor:
  check_interval: 60       # seconds between health checks
  crash_threshold: 3       # failures before alerting

alerts:
  enabled: true
  discord_channel: general-alerts

auth:
  token: "REDACTED"
```

---

## Field Descriptions

| Field                        | Type        | Required | Description |
|-----------------------------|-------------|----------|-------------|
| `game`                      | string      | ✅       | Game type (e.g., `ark`, `rust`, `valheim`) |
| `server_id`                 | string      | ✅       | Globally unique server identifier used in bot commands |
| `map`                       | string      | ❌       | Map or region name (optional but useful for context) |
| `cloud_target`              | string      | ❌       | Cloud destination for backups (e.g., s3, dropbox, b2) |
| `auto_update`               | bool        | ❌       | Enables/disables agent self-update feature |
| `env`                       | map         | ❌       | Key-value environment variables injected at runtime |
| `backup.path`               | string      | ✅       | Absolute path to game save or data directory |
| `backup.schedule.type`      | string      | ✅       | Schedule type (currently only `cron` is supported) |
| `backup.schedule.expression`| string      | ✅       | Cron-style string (e.g., `"0 * * * *"`) |
| `backup.schedule.timezone`  | string      | ✅       | Timezone in IANA format (`UTC`, `America/New_York`) |
| `backup.retention_days`     | int         | ✅       | Number of days to keep old backups |
| `monitor.check_interval`    | int (sec)   | ✅       | Interval between health checks |
| `monitor.crash_threshold`   | int         | ✅       | Failures before crash alert triggers |
| `alerts.enabled`            | bool        | ✅       | Enable/disable alert publishing |
| `alerts.discord_channel`    | string      | ❌       | Discord channel override for alerts |
| `auth.token`                | string      | ✅       | JWT or pre-shared token for agent authentication |

---

## Per-Game Customization Notes

Game profiles support optional or extended fields specific to each game.

### ARK: Survival Ascended

```yaml
mod_dir: /home/container/Mods
```
- mod_dir: Custom mod directory path

### ARK: Rust
```yaml
oxide_enabled: true
```

### Valheim
- Minimal profile. Only uses monitor and backup

---

## Validation Rules

The following rules are enforced by the agent on startup:

- `server_id` must be unique and match bot command inputs
- `schedule.expression` must be a valid cron expression
- All directory paths (e.g., `backup.path`, `mod_dir`) must be absolute
- `auth.token` must be present and valid
- All required fields must be present and of correct types
- Agent will refuse to start if the configuration is malformed

---

## Extensibility

The config format is designed for future-proofing. Optional and planned extensions include:

| Field/Feature        | Type     | Phase   | Notes |
|----------------------|----------|---------|-------|
| `cloud_target`       | string   | Phase 6 | e.g., `s3`, `dropbox`, `b2` |
| `auto_update`        | bool     | Phase 6 | Controls whether agent pulls updates |
| `env`                | map      | Phase 6 | Inject environment variables at runtime |
| `alert_hooks`        | object   | Phase 6 | Trigger on events like join, death, crash |
| `ports`, `processes` | object   | Phase 7 | Auto-detect features for new games |

---

## Sample Game Profiles

### ark.yaml

```yaml
game: ark
server_id: ark-west-001
map: Ragnarok

cloud_target: s3
auto_update: false

env:
  DEBUG: true
  REGION: us-east-1

backup:
  path: /home/container/ShooterGame/Saved
  schedule:
    type: cron
    expression: "0 */2 * * *"
    timezone: UTC
  retention_days: 5

monitor:
  check_interval: 120
  crash_threshold: 2

alerts:
  enabled: true
  discord_channel: ark-alerts

auth:
  token: "REDACTED"

mod_dir: /home/container/Mods
```

### rust.yaml

```yaml
game: rust
server_id: rust-east-001
map: Procedural Map

cloud_target: s3
auto_update: false

env:
  DEBUG: true
  REGION: us-east-1

backup:
  path: /home/container/serverdata
  schedule:
    type: cron
    expression: "0 * * * *"
    timezone: UTC
  retention_days: 7

monitor:
  check_interval: 60
  crash_threshold: 3

alerts:
  enabled: true

auth:
  token: "REDACTED"

oxide_enabled: true
```

### valheim.yaml

```yaml
game: valheim
server_id: valheim-test-001

cloud_target: s3
auto_update: false

env:
  DEBUG: true
  REGION: us-east-1

backup:
  path: /home/container/.config/unity3d/IronGate/Valheim/worlds
  schedule:
    type: cron
    expression: "30 * * * *"
    timezone: UTC
  retention_days: 3

monitor:
  check_interval: 90
  crash_threshold: 3

alerts:
  enabled: false

auth:
  token: "REDACTED"
```
