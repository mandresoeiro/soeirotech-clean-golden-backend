from pathlib import Path
import os
from datetime import timedelta

# --------------------------------------------------
# 📁 Diretório base do projeto
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --------------------------------------------------
# 🔐 Configurações básicas
# --------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# ---------------------------------------------------------------------
# 📦 Aplicativos instalados
# ---------------------------------------------------------------------
INSTALLED_APPS = [
    # apps Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # libs externas
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",  # 🔍 documentação automática OpenAPI

    # apps internos
    "accounts",
    "system",
    "integrations",
    "security",


    # ferramentas de apoio
    "django_extensions",
]

# ---------------------------------------------------------------------
# ⚙️ Configurações REST Framework
# ---------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# ---------------------------------------------------------------------
# 🔐 Configurações JWT
# ---------------------------------------------------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ---------------------------------------------------------------------
# 🧱 Middleware
# ---------------------------------------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # deve vir antes do CommonMiddleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ---------------------------------------------------------------------
# 🌍 CORS
# ---------------------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ apenas em dev
# Em produção:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:4200",
#     "https://meuapp.com",
# ]

# ---------------------------------------------------------------------
# 🌐 URLs e Templates
# ---------------------------------------------------------------------
ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ---------------------------------------------------------------------
# 🗄️ Banco de Dados (SQLite para dev)
# ---------------------------------------------------------------------
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# ---------------------------------------------------------------------
# 🗄️ Banco de Dados — PostgreSQL via Docker
# ---------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "soeirotech_db"),
        "USER": os.getenv("POSTGRES_USER", "soeirotech_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "soeirotech_pass"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}
# # ---------------------------------------------------------------------
# # 📡 Configurações de Email
# # ---------------------------------------------------------------------
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "soeirotech@gmail.com")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "soeirotech123")



# ---------------------------------------------------------------------
# 🌎 Localização
# ---------------------------------------------------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------
# 📂 Arquivos estáticos
# ---------------------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------
# 👤 Modelo de usuário personalizado
# ---------------------------------------------------------------------
AUTH_USER_MODEL = "accounts.User"
