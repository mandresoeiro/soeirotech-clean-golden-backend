from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# DRF com interface navegável (para testes locais)
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
    "rest_framework.renderers.BrowsableAPIRenderer"
)
