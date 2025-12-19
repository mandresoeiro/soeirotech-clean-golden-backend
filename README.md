# SoeiroTech Clean Golden Backend (Template)

Este repositório é um template profissional para projetos Django + DRF, pronto para produção, com autenticação JWT, PostgreSQL, Redis e Docker Compose.

## O que NÃO subir neste template
- Dados sensíveis (senhas, chaves, tokens)
- Arquivo `.env` (suba apenas `.env.example`)
- Banco de dados (arquivos `.sqlite3`, dumps, backups)
- Pastas de cache e build (`__pycache__`, `staticfiles/`, `media/`, `node_modules/`, etc.)
- Arquivos de usuário/editor (`.vscode/`, `.idea/`, etc.)
- Logs, arquivos temporários, arquivos de backup (`*.log`, `*.tmp`, `*.bak`)
- Coleções Postman com dados reais

## O que DEVE subir
- Código fonte (apps, settings, scripts)
- Dockerfile, docker-compose.yml
- `pyproject.toml`, `poetry.lock` (exceto se for privado)
- Scripts utilitários (exemplo: `/scripts/*.sh`)
- Arquivo `.env.example` com variáveis obrigatórias
- README.md completo
- Testes automatizados
- Templates de collection Postman sem dados sensíveis

## Como usar este template
1. Clique em "Use this template" no GitHub para criar seu projeto.
2. Clone o novo repositório.
3. Copie `.env.example` para `.env` e configure as variáveis.
4. Siga as instruções do README para rodar localmente.

## Estrutura recomendada
- `/backend` — código Django
- `/scripts` — scripts utilitários
- `/soeirotech-clean-base` — coleções e exemplos
- `.gitignore` — já configurado para template

## Licença
MIT

---
SoeiroTech © 2025
