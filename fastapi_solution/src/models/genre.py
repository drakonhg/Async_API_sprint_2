from .base import Config, BaseRoleMixin
from uuid import UUID


class Genre(Config):
    id: UUID = None
    name: str = None
    description: str = None


class GenreShort(BaseRoleMixin):
    pass
