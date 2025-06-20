# ReconSync Bot-Agent Protocol Specification

This document defines the communication protocol between the Discord-integrated **ReconSync Bot** and the distributed **Recon Agents** deployed on individual game servers (e.g., ARK, Rust, Valheim).

---

## 🔧 Purpose

This protocol enables the bot to dispatch commands (e.g., `/backup now`, `/status`) to agents and receive telemetry or alerts in return. It provides a secure, extensible, and structured communication mechanism for managing and monitoring game servers.

---

## 1. Transport Layer

### MVP Transport: **REST API (HTTP)**
- Stateless communication
- Easy to implement and debug
- Works over standard HTTPS

### Future Upgrades
- Phase 3+: WebSocket for persistent connections
- Phase 4+: Message Queues (RabbitMQ, RedisMQ) for reliability and async handling

---

## 2. Authentication & Security

### Agent Authentication
- Each request must include an `auth.token` from `config.yaml`
- Sent as HTTP header: `Authorization: Bearer <token>`

### Token Types
- **Phase 2 (MVP)**: Pre-shared token (defined per-agent)
- **Phase 3+**: JWT tokens with expiration, issuer verification

### Optional Future Enhancements
- IP whitelisting
- Signed payloads (HMAC or RSA)
- Rate limiting by IP or server ID

---

## 3. Message Types

### `heartbeat`
Sent at regular intervals to indicate agent is alive.

```json
{
  "type": "heartbeat",
  "server_id": "ark-west-001",
  "timestamp": "2025-06-19T12:00:00Z",
  "agent_version": "0.2.1",
  "uptime_sec": 86400,
  "os": "linux",
  "game": "ark",
  "config_hash": "d41d8cd98f00b204e9800998ecf8427e"
}
```

### `status_response`

```json
{
  "type": "status_response",
  "server_id": "rust-east-001",
  "timestamp": "2025-06-19T12:03:00Z",
  "payload": {
    "cpu": "15%",
    "ram": "2.1 GB",
    "process_health": "running"
  }
}
```

### `backup_result`

```json
{
  "type": "backup_result",
  "server_id": "ark-west-001",
  "timestamp": "2025-06-19T12:10:00Z",
  "payload": {
    "status": "success",
    "duration_sec": 87,
    "filename": "backup_ark-west-001_20250619.zip"
  }
}
```

### `crash_alert`

```json
{
  "type": "crash_alert",
  "server_id": "valheim-test-001",
  "timestamp": "2025-06-19T13:00:00Z",
  "payload": {
    "message": "Server unresponsive 3 times in a row",
    "threshold": 3,
    "action_taken": "none"
  }
}
```

### `agent_register`(Phase 3+)
Sent to bootstrap new agent with bot.

---

## 4. Request Routing
- The bot issues POST requests to the agent:
``` bash
POST /agent/<server_id>/command
```
- Request body:
```json
{
  "command": "backup",
  "timestamp": "2025-06-19T12:00:00Z"
}
```
-Agent responds synchronously (2xx + JSON) or asynchronously via webhook.

---

## 5. Payload Format
All responses from agent follow this base structure:
```json
{
  "server_id": "ark-west-001",
  "timestamp": "2025-06-19T12:00:00Z",
  "type": "backup_result",
  "payload": {
    "status": "success",
    "duration_sec": 87,
    "filename": "backup_ark-west-001_20250619.zip"
  }
}
```

### Standard Fields

| Field           | Description                        |
| --------------- | ---------------------------------- |
| `server_id`     | Matches the YAML config            |
| `timestamp`     | ISO-8601 format                    |
| `type`          | One of the defined message types   |
| `payload`       | Command- or event-specific payload |
| `agent_version` | (Optional) Agent version string    |
| `game`          | (Optional) Game type (ark, rust)   |

---

## 6. Error Handling
Agents return standard HTTP codes with a JSON body:
| HTTP Code | Meaning      | Notes                        |
| --------- | ------------ | ---------------------------- |
| `200`     | OK           | Success                      |
| `202`     | Accepted     | Processing async             |
| `400`     | Bad Request  | Invalid input                |
| `401`     | Unauthorized | Invalid/missing token        |
| `403`     | Forbidden    | Token valid, but not allowed |
| `500`     | Agent Error  | Internal failure             |
| `504`     | Timeout      | Agent operation stalled      |

### Example Error Payload
```json
{
  "server_id": "ark-west-001",
  "timestamp": "2025-06-19T12:01:00Z",
  "type": "error",
  "payload": {
    "status": "fail",
    "message": "Backup path does not exist",
    "details": "/home/container/ShooterGame/Saved"
  }
}
```

## 7. Agent Metadata Exchange
The following metadata is included in `heartbeat` and `agent_register` messages:
- agent_version
- os
- game
- uptime_sec
- config_hash

## 8. Extensibility Guidelines
- Future message types MUST define a new type
- Optional fields should not break parsers
- Agents should ignore unknown fields
- Backward compatibility is required for:
- heartbeat
- status_response
- backup_result
