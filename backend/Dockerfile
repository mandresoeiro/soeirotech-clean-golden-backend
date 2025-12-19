# ===============================================================
# 🐍 SoeiroTech Backend - Dockerfile Final Corrigido
# ---------------------------------------------------------------
# Base: Python 3.12-slim
# Gerenciador de pacotes: Poetry
# Banco: PostgreSQL (psycopg2-binary)
# Entrypoint: scripts/entrypoint.sh
# ===============================================================

FROM python:3.12-slim AS base

# --------------------------
# Diretório de trabalho
# --------------------------
WORKDIR /app

# --------------------------
# Variáveis de ambiente
# --------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# --------------------------
# Instalar dependências de sistema
# --------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# --------------------------
# Instalar Poetry
# --------------------------
RUN pip install --no-cache-dir poetry

# --------------------------
# Copiar arquivos de dependências
# --------------------------
