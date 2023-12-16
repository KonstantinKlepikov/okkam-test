#! /usr/bin/env bash
set -e

python data/init_db.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000