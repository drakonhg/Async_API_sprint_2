from typing import Optional

from .actor import Actor
from .base import BaseMixin
from .writer import Writer
from .genre import GenreShort


class Film(BaseMixin):
    title: str
    description: Optional[str] = None
    imdb_rating: Optional[float] = None

    genre: Optional[list[GenreShort]]
    actors_names: Optional[list[str]] = None
    writers_names: Optional[list[str]] = None

    actors: Optional[list[Actor]] = None
    writers: Optional[list[Writer]] = None
    director: Optional[list[str]] = []
