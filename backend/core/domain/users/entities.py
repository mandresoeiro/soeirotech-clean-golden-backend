from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserEntity:
    """
    Entidade pura de domínio.
    Representa um usuário de forma independente de frameworks.
    """
    id: Optional[int]
    email: str
    full_name: Optional[str] = ""
    is_active: bool = True
    is_verified: bool = False
    date_joined: Optional[datetime] = None

    def activate(self):
        """Ativa o usuário."""
        self.is_active = True

    def verify(self):
        """Marca o usuário como verificado."""
        self.is_verified = True
