# ReconSync Roadmap

> **Project:** ReconSync  
> **Purpose:** A cross-platform, Discord-integrated game server backup and monitoring tool  
> **Owner:** SoldierCity.io  
> **Last Updated:** 2025-06-19

---

## Overview

ReconSync is a bot-agent solution for server admins running games like ARK, Rust, and Valheim. It provides manual and automated backups, server monitoring, and Discord-based alerts or commands.

The project will be built in clear phases, starting with an MVP designed for quick delivery, feedback, and validation.

---

## ✅ Phase 1 – Planning & Architecture

**Goal:** Define what you're building, why, and how.

### Tasks
- [X] Create `ReconSync-Internal` private GitHub repo
- [X] Write `architecture.md` (MVP scope + high-level components)
- [X] Write `decision-log.md` (record major design decisions)
- [X] Define command structure in `commands.md`
- [X] Design YAML game profile format (`game_profiles.md`)
- [X] Draft initial game profiles (ARK, Rust)
- [X] Design bot/agent protocol
- [X] Select tech stack and deployment model

---

## 🔹 Phase 2 – MVP Development (Agent + Bot)

**Goal:** Create a working MVP with basic backup and monitoring via Discord.

### Agent (`agent/`)
- [ ] Create `ReconSync` public GitHub repo
- [ ] Scaffold `agent/` directory with placeholders: `serve.py`, `backup.py`, `monitor.py`
- [ ] `backup.py`: performs file zips and local backups
- [ ] `monitor.py`: detects server status, ports, resources
- [ ] Load and validate `config.yaml`
- [ ] Discord webhook alert system
- [ ] Add changelog and internal logging
- [ ] Implement auth token validation and TLS proxy enforcement
- [ ] Document token generation, rotation strategy, and security notes

### Discord Bot (`bot/`)
- [ ] Scaffold `bot/` directory with `main.py`, command stubs, and `dispatcher.py
- [ ] `main.py`: Discord bot with slash commands
- [ ] `/backup now` command
- [ ] `/status` command
- [ ] Implement Discord permission gating
- [ ] Send alerts via webhook or bot messages
- [ ] Add internal logging

### Config & Templates
- [ ] `config.yaml` for each server
- [ ] Game profiles: `ark.yaml`, `rust.yaml`
- [ ] Test on both Linux and Windows

### Documentation & Versioning
- [ ] Start internal changelog tracking for v0.1.0 (docs/changelog.md)
- [ ] Add version headers and initial release notes

---

## 🔹 Phase 3 – Developer Infrastructure

**Goal:** Ensure project is maintainable, testable, and developer-friendly.

### Tasks
- [ ] `.gitignore`, `.env.example`, `requirements.txt`
- [ ] Setup `install.sh` and `install.bat` for quick installs
- [ ] Add basic test scripts or pytest stubs
- [ ] Versioning and changelog standards
- [ ] Create `schema.yaml` definition for config files
- [ ] Add automated validation using `jsonschema` or equivalent
- [ ] Write unit test to validate `games/*.yaml` against schema

---

## 🔹 Phase 4 – Public GitHub Release (v0.1.0)

**Goal:** Release a self-hosted open-source MVP.

### Tasks
- [ ] `README.md` with clear features and screenshots
- [ ] User documentation in `docs/user/`
- [ ] Per-game setup guides
- [ ] GitHub Issues or Project Board
- [ ] MIT or Apache 2.0 License

---

## 🔹 Phase 5 – Marketing & Community Engagement

**Goal:** Attract early users, drive adoption, and collect feedback.

### Tasks
- [ ] Landing page at `SoldierCity.io/ReconSync`
- [ ] Create a roadmap of future functionality that is advertised to the user base
- [ ] Register bot on Top.gg and Discord directories
- [ ] Announce in game server admin subreddits & Discords
- [ ] Walkthrough videos or demo GIFs
- [ ] Collect testimonials or bug reports
- [ ] Early access program for hosted (SaaS) users
      
---

## 🔹 Phase 6 – Premium Feature Development (v1.x)

**Goal:** Add premium features and infrastructure.

### Tasks
- [ ] S3, Dropbox, or B2 cloud backup targets
- [ ] `/restore` command for recoveries
- [ ] Multiple server support per bot
- [ ] Permission and auth system
- [ ] Dynamic command registration
- [ ] Game profile templates per server
- [ ] Discord notifications (join/death/crash)
- [ ] Web dashboard
- [ ] Add UI schema support for dynamic config generation
- [ ] Upgrade token system to JWTs with expiration and issuer verification
- [ ] Integrate with optional secret manager for agent authentication

### Premium Infrastructure
- [ ] Stripe integration
- [ ] Hosted dashboard (optional)
- [ ] License key or premium tier support
- [ ] SaaS Hosting: Provide managed ReconSync instance for Discord servers

---

## 🔹 Phase 7 – Expansion & Maintenance

**Goal:** Improve UX, add more games, and enable community contribution.

### Tasks
- [ ] Enable agent to auto-download updated schema for self-validation
- [ ] Add game profiles: Valheim, 7DTD, Minecraft, etc.
- [ ] Auto-detect profiles based on ports/processes
- [ ] Optional GUI or hosted dashboard
- [ ] Contributor guide and code of conduct
- [ ] `SECURITY.md` for responsible disclosures   

---

## Suggested Project Structure

```bash
reconsync/
├── agent/
│   ├── backup.py
│   ├── monitor.py
│   └── config.yaml
├── bot/
│   └── main.py
├── games/
│   ├── ark.yaml
│   └── rust.yaml
├── docs/
│   ├── user/
│   └── dev/
├── scripts/
│   ├── install.sh
│   └── install.bat
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```
