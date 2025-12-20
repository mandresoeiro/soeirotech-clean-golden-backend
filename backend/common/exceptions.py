"""
common.exceptions
-----------------
Exceções personalizadas reutilizáveis no backend SoeiroTech Clean Golden™.
"""
from rest_framework.exceptions import APIException

class BusinessLogicError(APIException):
    """Erro de regra de negócio genérico."""
    status_code = 400
    default_detail = "Ocorreu um erro de lógica de negócio."
    default_code = "business_logic_error"

class ValidationError(APIException):
    """Erro de validação customizada."""
    status_code = 422
    default_detail = "Dados inválidos fornecidos."
    default_code = "validation_error"
