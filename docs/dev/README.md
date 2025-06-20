# ReconSync Developer Documentation

This folder contains **developer-focused design documentation** for the ReconSync project — a modular, Discord-integrated bot and agent system for monitoring and backing up game servers like ARK, Rust, and Valheim.

These docs define the system architecture, command interface, config formats, communication protocols, and tech stack. They are intended for internal contributors, maintainers, and collaborators working on the codebase.

> If you're looking for user setup guides or installation instructions, visit [`docs/user/`](../user/) (coming soon).

---

## Document Index

### Core Design

- [System Architecture](architecture.md)  
  High-level overview of the bot, agent, command dispatcher, and communication model.

- [Bot-Agent Protocol](bot-agent-protocol.md)  
  REST API used for communication between the Discord bot and game server agents.

- [Game Profile Format](game_profiles.md)  
  YAML config structure used by each Recon Agent to manage game-specific monitoring and backups.

- [Slash Command Reference](commands.md)  
  Full list of supported slash commands (`/status`, `/backup now`, etc.) with arguments and permissions.

- [Tech Stack & Deployment Model](tech_stack.md)  
  Describes key Python libraries, deployment options (Docker, systemd), and future extensibility.

---

### Planning & Change Tracking

- [Roadmap](roadmap.md)  
  Publicly shareable milestones and phase-based feature planning.

- [Design Decision Log](decision-log.md)  
  Running log of major architectural and feature decisions made during the project.

- [Changelog](changelog.md)  
  Tracks non-code design and documentation updates that affect architecture or user-facing behavior.

---

## Notes

- Changes to commands or config formats should be reflected in both:
  - [commands.md](commands.md)
  - [game_profiles.md](game_profiles.md)
- Roadmap changes should align with tracked milestones in [roadmap.md](roadmap.md)
- Long-form planning and internal phase breakdowns are maintained offline

---

## Access and Privacy

These documents are safe for inclusion in the public repo, but sensitive tokens and security secrets are excluded by design. Please do not commit agent secrets, Discord tokens, and other credentials to this repository.

---
