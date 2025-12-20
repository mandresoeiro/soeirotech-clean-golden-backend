"""
common.utils
-------------
Funções utilitárias independentes e genéricas.
"""
import uuid
from datetime import datetime

def generate_uuid() -> str:
    """Gera um UUID único em formato string."""
    return str(uuid.uuid4())

def current_timestamp() -> str:
    """Retorna o timestamp UTC atual em formato ISO."""
    return datetime.utcnow().isoformat() + "Z"
