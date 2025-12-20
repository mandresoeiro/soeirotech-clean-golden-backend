✅ O que este código cobre

Função	Endpoint	Método	Proteção

Criar usuário	/api/accounts/users/	POST	Público

Listar usuários	/api/accounts/users/	GET	JWT opcional

Ativar usuário	/api/accounts/users/{id}/activate/	POST	JWT

Verificar e-mail	/api/accounts/users/{id}/verify/	POST	JWT

Perfil logado	/api/accounts/users/me/	GET	JWT

Atualizar perfil	/api/accounts/users/update_profile/	PATCH	JWT

Trocar senha	/api/accounts/users/change_password/	PUT	JWT

