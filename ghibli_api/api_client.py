import requests

from ghibli_api.enums import Urls


class ApiClient:
    @staticmethod
    def get_all_films_response():
        all_films_response = requests.get(Urls.FILMS_URL.value)
        return all_films_response

    @staticmethod
    def get_all_people_response():
        all_films_response = requests.get(Urls.PEOPLE_URL.value)
        return all_films_response
