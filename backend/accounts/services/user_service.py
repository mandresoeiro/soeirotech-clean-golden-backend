from core.domain.users.services import UserService as DomainUserService


class AccountApplicationService:
    """Adapta o serviço de domínio para uso na camada Django/DRF."""

    @staticmethod
    def create_user(email: str, full_name: str = "", password: str = None):
        return DomainUserService.create_user(email=email, full_name=full_name, password=password)

    @staticmethod
    def activate_user(user_id: int):
        return DomainUserService.activate_user(user_id)

    @staticmethod
    def verify_email(user_id: int):
        return DomainUserService.verify_email(user_id)
