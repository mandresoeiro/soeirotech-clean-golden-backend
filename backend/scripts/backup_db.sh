#!/bin/sh
set -e

# Realiza backup do banco SQLite
cp /app/db.sqlite3 /backup/db.sqlite3_$(date +%Y%m%d%H%M%S)
