from enum import Enum, IntEnum, unique


@unique
class Urls(Enum):
    BASE_URL = "https://ghibliapi.herokuapp.com"
    FILMS_URL = f"{BASE_URL}/films"
    PEOPLE_URL = f"{BASE_URL}/people"


@unique
class ResponseCode(IntEnum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500
