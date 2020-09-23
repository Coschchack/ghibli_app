from enum import Enum, unique


@unique
class Urls(Enum):
    BASE_URL = "https://ghibliapi.herokuapp.com"
    FILMS_URL = f"{BASE_URL}/films"
    PEOPLE_URL = f"{BASE_URL}/people"
