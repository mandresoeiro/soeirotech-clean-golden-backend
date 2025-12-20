#!/bin/sh
set -e

# Executa seeds do banco de dados
python manage.py loaddata initial_data.json
