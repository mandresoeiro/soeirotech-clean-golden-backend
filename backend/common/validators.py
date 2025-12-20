"""
common.validators
-----------------
Funções de validação reutilizáveis.
"""
import re
from rest_framework.exceptions import ValidationError

def validate_cpf(value: str) -> str:
    """Valida CPF em formato simples (sem pontuação)."""
    if not re.match(r"^\d{11}$", value):
        raise ValidationError("CPF deve conter 11 dígitos numéricos.")
    return value

def validate_non_empty(value: str) -> str:
    """Garante que o valor não seja vazio."""
    if not value or not value.strip():
        raise ValidationError("Campo não pode estar vazio.")
    return value
