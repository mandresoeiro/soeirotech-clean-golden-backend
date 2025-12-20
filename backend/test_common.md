🧩 Referência visual mental
soeirotech-clean-base/
├── backend/
│   ├── manage.py
│   ├── core/
│   ├── common/
│   ├── test_common.py  ← ⚠️ arquivo deve estar aqui
└── docs/


Então:

Se você está aqui → soeirotech-clean-base/
👉 use python backend/manage.py shell < backend/test_common.py

Se você está aqui → soeirotech-clean-base/backend/
👉 use python manage.py shell < test_common.py

✅ Checklist final da correção
Ação	Comando	Status
Verificar pasta atual	pwd	☐
Confirmar existência do arquivo	`ls backend	grep test_common.py`
Executar comando correto	(um dos dois acima)	☐
Ver saída “✅ Todos os testes básicos...”	esperado	☐



#TODO SAIDA ESPERADA
✅ Todos os testes básicos...

============================================================
🔍 TESTE AUTOMATIZADO DO MÓDULO COMMON INICIADO
============================================================

[UTILS]
UUID: 98b4c4a2-60f9-4381-b88d-4a3237e3a1e2
Timestamp: 2025-12-19T14:48:23.091Z

[VALIDATORS]
CPF válido: 12345678901
Campo válido: Marcio
Erro esperado: [ErrorDetail(string='CPF deve conter 11 dígitos numéricos.', code='invalid')]

[EXCEPTIONS]
Erro capturado corretamente: Operação não permitida.

[SERIALIZERS]
BaseSerializer: {'message': 'Sucesso'}
TimestampSerializer campos: {'created_at': DateTimeField(read_only=True), 'updated_at': DateTimeField(read_only=True)}

[MIXINS]
TimestampMixin: TimestampMixin
ResponseMixin: ResponseMixin

✅ Todos os testes básicos do módulo 'common' foram executados com sucesso.
============================================================

