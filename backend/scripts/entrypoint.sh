#!/bin/bash
# ==============================================================
# 🎯 SoeiroTech Backend Entrypoint
# --------------------------------------------------------------
# Executa migrações, cria superusuário e inicia o servidor Django
# ==============================================================

set -e

echo "🔧 Aplicando migrações..."
python manage.py migrate --noinput

echo "👤 Verificando superusuário..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
email = "admin@soeirotech.dev"
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(
        email=email,
        full_name="Administrador",
        password="admin123"
    )
    print("✅ Superusuário criado: admin@soeirotech.dev / admin123")
else:
    print("ℹ️ Superusuário já existe, pulando criação.")
END

echo "🚀 Iniciando servidor Django..."
python manage.py runserver 0.0.0.0:8000
