#!/usr/bin/env bash
# Basic install script for ReconSync

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Virtual environment ready."