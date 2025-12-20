from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import UserEntity


class IUserRepository(ABC):
    """Contrato de repositório para o domínio de usuários."""

    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def list_all(self) -> List[UserEntity]:
        pass
