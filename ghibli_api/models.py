from dataclasses import dataclass, field
from typing import List


@dataclass
class PeopleToMovieMap:
    movie_title: str
    people: List = field(default_factory=list)
