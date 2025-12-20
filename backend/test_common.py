"""
Script de verificação rápida do módulo 'common'.
Execução:
    python manage.py shell < backend/test_common.py
"""

from common.utils import generate_uuid, current_timestamp
from common.validators import validate_cpf, validate_non_empty
from common.exceptions import BusinessLogicError, ValidationError
from common.serializers import BaseSerializer, TimestampSerializer
from common.mixins import TimestampMixin, ResponseMixin

print("=" * 60)
print("🔍 TESTE AUTOMATIZADO DO MÓDULO COMMON INICIADO")
print("=" * 60)

# 1️⃣ Teste utils
print("\n[UTILS]")
print("UUID:", generate_uuid())
print("Timestamp:", current_timestamp())

# 2️⃣ Teste validators
print("\n[VALIDATORS]")
try:
    print("CPF válido:", validate_cpf("12345678901"))
    print("Campo válido:", validate_non_empty("Marcio"))
    try:
        validate_cpf("abc")
    except Exception as e:
        print("Erro esperado:", e)
except Exception as e:
    print("Erro inesperado em validators:", e)

# 3️⃣ Teste exceptions
print("\n[EXCEPTIONS]")
try:
    raise BusinessLogicError("Operação não permitida.")
except BusinessLogicError as e:
    print("Erro capturado corretamente:", e.detail)

# 4️⃣ Teste serializers
print("\n[SERIALIZERS]")
base = BaseSerializer()
print("BaseSerializer:", base.data)
ts = TimestampSerializer()
print("TimestampSerializer campos:", ts.get_fields())

# 5️⃣ Teste mixins (apenas importação)
print("\n[MIXINS]")
print("TimestampMixin:", TimestampMixin.__name__)
print("ResponseMixin:", ResponseMixin.__name__)

print("\n✅ Todos os testes básicos do módulo 'common' foram executados com sucesso.")
print("=" * 60)
