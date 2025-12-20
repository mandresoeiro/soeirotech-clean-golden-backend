from core.domain.users.entities import UserEntity
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


class UserService:
    """Camada de serviço conectando DRF ao domínio limpo."""

    @staticmethod
    def _to_entity(user: User) -> UserEntity:
        return UserEntity(
            id=user.id,
            email=user.email,
            full_name=getattr(user, "full_name", ""),
            is_active=user.is_active,
            is_verified=getattr(user, "is_verified", False),
            date_joined=user.date_joined,
        )

    @staticmethod
    def create_user(email: str, full_name: str = "", password: str = None) -> UserEntity:
        if not email:
            raise ValueError("O campo e-mail é obrigatório.")

        if User.objects.filter(email=email).exists():
            raise ValueError("Já existe um usuário com este e-mail.")

        user = User.objects.create_user(email=email, full_name=full_name, password=password)
        return UserService._to_entity(user)

    @staticmethod
    def activate_user(user_id: int) -> UserEntity:
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise ValueError("Usuário não encontrado.")

        user.is_active = True
        user.save(update_fields=["is_active"])
        entity = UserService._to_entity(user)
        entity.activate()
        return entity

    @staticmethod
    def verify_email(user_id: int) -> UserEntity:
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise ValueError("Usuário não encontrado.")

        user.is_verified = True
        user.save(update_fields=["is_verified"])
        entity = UserService._to_entity(user)
        entity.verify()
        return entity
