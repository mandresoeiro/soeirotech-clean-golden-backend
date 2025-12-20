Agora, vamos entender o papel de cada arquivo:

Arquivo	Função
exceptions.py	Classes personalizadas de erro (ex: BusinessLogicError, InvalidOperationError)
mixins.py	Classes auxiliares para views ou models (ex: TimestampMixin, SoftDeleteMixin)
utils.py	Funções utilitárias genéricas (ex: geração de tokens, manipulação de datas)
validators.py	Funções de validação reutilizáveis (ex: validar CPF, e-mail corporativo, etc.)
serializers.py	Serializers genéricos, normalmente herdados em outros módulos


🧩 Referência visual mental
┌──────────────────────────────────────────────┐
│ COMMON — Toolkit Interno                    │
│──────────────────────────────────────────────│
│ ⚠️ exceptions.py → Erros DRF personalizados │
│ 🧱 mixins.py → Timestamp + respostas padrão │
│ 🔧 utils.py → UUID + timestamps ISO         │
│ ✅ validators.py → CPF + campos obrigatórios│
│ 🧾 serializers.py → Base genérica DRF       │
└──────────────────────────────────────────────┘
