#!/bin/sh
set -e

# Executa migrações do Django
python manage.py migrate
